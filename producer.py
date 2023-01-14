import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=sys.argv[1] if len(sys.argv) >= 2 else 'Hellô!')

connection.close()
