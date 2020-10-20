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


@app.route('/')
def index():
    entries = models.Entries.select()
    return render_template('index.html', entries=entries)


@app.route('/entries')
def entries():
    return redirect(url_for('index'))


@app.route('/entries/<int:entry_id')
def detail(entry_id):
    try:
        entry = models.Entries.select().where(
            models.Entries.id == int(entry_id)
        ).get()
    except models.DoesNotExist:
        pass

    return render_template('details.html', entry=entry)


@app.route('/entries/new', methods=['GET', 'POST'])
def create_entry():
    form = forms.EntryForm()
    if form.validate_on_submit():
        entry_id = models.Entries.create_entry(
            title=form.title.data,
            date=form.date.data,
            time_spent=form.time_spent.data,
            what_you_learned=form.what_you_learned.data,
            resources_used=form.resources_used.data,
        )

        return redirect(url_for('detail', entry_id=entry_id))

    return render_template('new.html', form=form)









if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG)