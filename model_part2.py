from mongoengine import Document, StringField, BooleanField

import connect


class Contact(Document):
    fullname = StringField(required=True)
    email = StringField(unique=True)
    ck_sent = BooleanField(default=False)
    phone = StringField()
    meta = {"collection": "contacts"}
