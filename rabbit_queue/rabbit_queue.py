import pika


class RabbitQueue:
    def __init__(self, queue_name, host='localhost'):
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self._channel = self._connection.channel()
        self._queue_name = queue_name
        self._channel.queue_declare(queue=self._queue_name)

    def __del__(self):
        self._connection.close()

    def publish(self, body):
        self._channel.basic_publish(exchange='', routing_key=self._queue_name, body=body)

    def consume(self, callback):
        self._channel.basic_consume(queue=self._queue_name, on_message_callback=callback)
        self._channel.start_consuming()
