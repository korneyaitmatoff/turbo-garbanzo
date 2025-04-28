import uuid

from pika import (
    BlockingConnection,
    ConnectionParameters,
    BasicProperties
)


class RpcClient:
    def __init__(self, host: str, port: int):
        self.connection = BlockingConnection(
            ConnectionParameters(
                host=host,
                port=port,
            )
        )
        self.channel = self.connection.channel()

        result = self.channel.queue_declare("events")
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True
        )

        self.response = None
        self.corr_id = None

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, message: bytes) -> str:
        self.response = None
        self.corr_id = str(uuid.uuid4())

        self.channel.basic_publish(
            exchange="",
            routing_key="events",
            properties=BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id
            ),
            body=message
        )

        while self.response is None:
            self.connection.process_data_events()

        return self.response.decode()
