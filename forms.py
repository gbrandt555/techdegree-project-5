from flask_wtf import Form
from wtforms import StringField, DateTimeField
from wtforms.validators import DataRequired

from models import Entry

import datetime


class EntryForm(Form):
    journal_entry = StringField(
        'Entry',
        validators=[DataRequired()]
    )
    title_of_entry = StringField(
        'Title',
        validators=[DataRequired()]
    )
    date_of_entry = DateTimeField(default=datetime.datetime.now)
    time_spent = DateTimeField(default=0)
    what_you_learned = StringField(
        'What you learned',
        validators=[DataRequired()]
    )
    resources = StringField(
        'Resources',
        validators=[DataRequired()]
    )