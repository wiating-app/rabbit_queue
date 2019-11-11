import pika


class ImageQueue:
    def __init__(self, queue_name, host='localhost'):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()
        self.queue_name = queue_name
        self.channel.queue_declare(queue=self.queue_name)

    def __del__(self):
        self.connection.close()

    def publish(self, body):
        self.channel.basic_publish(exchange='', routing_key=self.queue_name, body=body)

    def consume(self, callback):
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=callback)
        self.channel.start_consuming()
