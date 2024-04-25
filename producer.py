import pika
from faker import Faker

from model_part2 import Contact
import connect

def main():
    # credentials = pika.PlainCredentials('guest', 'guest')
    # connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    # channel = connection.channel()

    # channel.queue_declare(queue='sending_emails_queue')

    fake = Faker()
    def fill_data(number: int) -> None:
        Contact.drop_collection()
        for _ in range(number):
            fullname = fake.name()
            email = fake.email()
            ck_sent = bool(0)
            phone = fake.phone_number()
            contact = Contact(fullname=fullname, email=email, ck_sent=ck_sent, phone=phone)            
            contact.save()
    
    fill_data(3)
    print("DONE.")


if __name__ == '__main__':
    main()
