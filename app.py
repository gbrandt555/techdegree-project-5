from flask import Flask, g, render_template, flash, redirect, url_for

import forms
import models, datetime

DEBUG = True


app = Flask(__name__)


@app.before_request
def before_request():
    """Connect to Database before each request"""
    g.db = models.DATABASE
    g.db.connect()



@app.after_request
def after_request(response):
    """Close Databse connection after each request"""
    g.db.close()
    return response


@app.route('/', methods='GET', 'POST')
def entry():
    form = forms.EntryForm()
    if form.validate_on_submit():
        flash("Entry successful!", "success")
        models.Entry.create_entry()
        return redirect(url_for('index'))
    return render_template('')


if __name__ == '__main__':
    models.initialize()
    models.Entry.create_entry(
        journal_entry='First entry',
        title_of_entry='Welcome',
        date_of_entry=datetime.datetime.now,
        time_spent=1,
        what_you_learned='How to create a journal entry',
        resources='Treehouse'
    )
    app.run(debug=DEBUG)