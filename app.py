from flask import Flask, g, render_template, flash, redirect, url_for

import forms
import models, datetime

DEBUG = True


app = Flask(__name__)
app.secret_key = 'dvsdf.,2.3,452fsdfoweifowihe0293.wefweom'

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


@app.route('/', methods=['GET', 'POST'])
def index():
    form = forms.EntryForm()
    return render_template('index.html', form=form)


@app.route('/new.html', methods=['GET', 'POST'])
def new_entry():
    form = forms.EntryForm()
    if form.validate_on_submit():
        flash("Entry successful!", "success")
        models.Entry.create_entry(
            journal_entry=form.journal_entry.data,
            title_of_entry=form.title_of_entry.data,
            date_of_entry=form.date_of_entry.default,
            time_spent=form.date_of_entry.default,
            what_you_learned=form.what_you_learned.data,
            resources=form.resources.data
        )
        return redirect(url_for('index'))
    return render_template('new.html', form=form)


if __name__ == '__main__':
    models.initialize()
    models.Entry.create_entry(
        journal_entry='First entry',
        title_of_entry='Welcome',
        date_of_entry=datetime.datetime.now(),
        time_spent=1,
        what_you_learned='How to create a journal entry',
        resources='Treehouse'
    )
    app.run(debug=DEBUG)