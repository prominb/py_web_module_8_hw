from faker import Faker
from model_part2 import Contact


fake = Faker()


def fill_data(number: int) -> None:
    Contact.drop_collection()
    for _ in range(number):
        record = Contact()
        record.fullname = fake.name()
        record.email = fake.email()
        record.ck_sent = bool(0)
        record.phone = fake.phone_number()
        record.save()

# if __name__ == '__main__':
#     fill_data()
