from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

from models import Entry


class EntryForm(Form):
    journal_entry = StringField(
        'Entry',
        validators=[
            DataRequired(),
        ]
    )