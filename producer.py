from random import randint
from bson.objectid import ObjectId

import pika
from faker import Faker

from model_part2 import Contact
import connect


def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='sending_emails_queue')

    number = randint(5, 10)
    fake = Faker()
    Contact.drop_collection()
    for _ in range(number):
        fullname = fake.name()
        email = fake.email()
        ck_sent = bool(0)
        phone = fake.phone_number()
        contact = Contact(fullname=fullname, email=email, ck_sent=ck_sent, phone=phone)            
        contact.save()
        channel.basic_publish(exchange='', routing_key='sending_emails_queue', body=f"{contact.id}")

    connection.close()
    print("DONE.")


if __name__ == '__main__':
    main()
