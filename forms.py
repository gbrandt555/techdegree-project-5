from flask_wtf import Form
from wtforms import StringField, DateTimeField, IntegerField, TextAreaField
from wtforms.validators import DataRequired

from models import Entries

import datetime


class EntryForm(Form):
    title = StringField(
        'Title',
        validators=[DataRequired()]
    )
    date = DateTimeField(
        'Date',
    )
    time_spent = IntegerField(
        'Time Spent',
        validators=[DataRequired()]
    )
    what_you_learned = TextAreaField(
        'What You Learned'
    )
    resources_used = TextAreaField(
        'Resources Used'
    )