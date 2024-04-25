from mongoengine import Document, StringField, BooleanField

import connect


class Contact(Document):
    fullname = StringField(required=True)
    email = StringField(unique=True)
    ck_sent = BooleanField(default=False)
    phone = StringField()

    # born_date = StringField(max_length=50)
    # born_location = StringField(max_length=150)
    # description = StringField()
    meta = {"collection": "contacts"}
