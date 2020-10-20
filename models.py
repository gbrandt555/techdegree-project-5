import datetime

from peewee import *


DATABASE = SqliteDatabase('journal.db')


class Entries(Model):
    title = CharField(max_length=150)
    date = DateTimeField(default=datetime.datetime.now)
    time_spent = CharField(max_length=20)
    what_you_learned = TextField()
    resources_used = TextField()

    class Meta:
        database = DATABASE
        order_by = ('-date_of_entry',)

    @classmethod
    def create_entry(cls, title, date, time_spent, what_you_learned, resources_used):
        entry = cls.create(
            title=title,
            date=date,
            time_spent=time_spent,
            what_you_learned=what_you_learned,
            resources_used=resources_used,
        )
        return entry.id


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Entries], safe=True)
    DATABASE.close()

