from faker import Faker
from model_part2 import Contact


fake = Faker()


def fill_data():
    Contact.drop_collection()
    for i in range(5):
        record = Contact()
        record.fullname = fake.name()
        record.email = fake.email()
        record.ck_sent = bool(0)
        record.phone = fake.phone_number()
        record.save()
