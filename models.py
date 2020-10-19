import datetime

from peewee import *


DATABASE = SqliteDatabase('journal.db')


class Entry(Model):
    journal_entry = CharField(unique=False)
    title_of_entry = CharField(unique=False)
    date_of_entry = DateTimeField(default=datetime.datetime.now)
    time_spent = IntegerField(default=0)
    what_you_learned = CharField(unique=False)
    resources = CharField(unique=False)

    class Meta:
        database = DATABASE
        order_by = ('-date_of_entry',)

    @classmethod
    def create_entry(cls, journal_entry, title_of_entry, date_of_entry, time_spent, what_you_learned, resources):
        cls.create(
            journal_entry=journal_entry,
            title_of_entry=title_of_entry,
            date_of_entry=date_of_entry,
            time_spent=time_spent,
            what_you_learned=what_you_learned,
            resources=resources
        )


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Entry], safe=True)
    DATABASE.close()

