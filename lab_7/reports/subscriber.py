import pika

from datetime import datetime
from json import dumps

from src.service import prepare_report
from src.client import get_all_data
from src.minio_client import load_report

from src.config import (
    RMQ_PORT,
    RMQ_HOST
)


def on_request(ch, method, props, body):
    print(f"Received request: {body.decode()}")

    filename = f"report_{datetime.now()}.json"
    with open(filename, "w") as f:
        data = get_all_data()["data"]
        f.write(dumps(prepare_report(data=data)))

    load_report(
        object_name=filename,
        filepath=filename
    )

    ch.basic_publish(
        exchange="",
        routing_key=props.reply_to,
        properties=pika.BasicProperties(correlation_id=props.correlation_id),
        body=filename
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)


try:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RMQ_HOST, port=RMQ_PORT))
    channel = connection.channel()

    channel.queue_declare(queue="events")

    # channel.basic_consume(prefetch_count=1)
    channel.basic_consume(queue="events", on_message_callback=on_request)

    print(" [x] Awaiting RPC requests")
    channel.start_consuming()
except Exception as e:
    print(e)
    print(f"Try connect to {RMQ_HOST}:{RMQ_PORT}")
