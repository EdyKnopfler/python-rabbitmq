import pika
import sys
import os


def callback(ch, method, properties, body):
    print(body.decode('utf-8'))


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    channel.basic_consume(queue='hello',
                          auto_ack=True,
                          on_message_callback=callback)
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
