from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, TextAreaField
from wtforms.validators import DataRequired

from models import Entries

import datetime


class EntryForm(FlaskForm):
    title = StringField(
        'Title',
        validators=[DataRequired()]
    )
    date = DateField(
        'Date (YYYY-MM-DD)',
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