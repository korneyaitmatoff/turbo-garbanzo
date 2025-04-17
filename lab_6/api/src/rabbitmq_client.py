import asyncio
import functools

from pika import ConnectionParameters, BlockingConnection

from src.config import (
    RMQ_HOST,
    RMQ_PORT
)

params = ConnectionParameters(
    host=RMQ_HOST,
    port=RMQ_PORT
)


def sync(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.get_event_loop().run_until_complete(f(*args, **kwargs))

    return wrapper


def publish(body: bytes):
    with BlockingConnection(params) as connection:
        with connection.channel() as ch:
            ch.queue_declare(queue="events")
            ch.basic_publish(
                exchange="",
                routing_key="events",
                body=body
            )
            ch.close()
        connection.close()


def subscribe():
    def process_message(*args):
        for arg in args:
            if isinstance(arg, bytes):
                print(arg)

    with BlockingConnection(params) as connection:
        with connection.channel() as ch:
            ch.queue_declare(queue="events")
            ch.basic_consume(
                queue="events",
                on_message_callback=process_message
            )
            print("Wait messages")
            ch.start_consuming()

            ...


publish(
    body=b"report"
)
