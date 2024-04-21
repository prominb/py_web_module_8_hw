from mongoengine import Document, StringField, BooleanField


class Contact(Document):
    fullname = StringField(required=True, unique=True)
    email = StringField()
    ck_sent = BooleanField(default=False)
    phone = StringField()

    # born_date = StringField(max_length=50)
    # born_location = StringField(max_length=150)
    # description = StringField()
    meta = {"collection": "contacts"}
