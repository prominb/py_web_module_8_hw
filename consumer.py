import os
import sys

import pika

from model_part2 import Contact
import connect


def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='sending_emails_queue')

    def callback(ch, method, properties, body):
        contact_id = body.decode()
        contact = Contact.objects.with_id(contact_id)
        print(f"For ContactID: {contact_id}", end=" | ")
        contact.update(set__ck_sent=True)
        print(f"Message sent to {contact.email}.")

    channel.basic_consume(queue='sending_emails_queue', on_message_callback=callback, auto_ack=True)

    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
