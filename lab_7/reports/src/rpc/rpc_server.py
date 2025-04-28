import pika

from src.config import (
    RMQ_PORT,
    RMQ_HOST
)


def on_request(ch, method, props, body):
    print(f"Received request: {body.decode()}")
    response = f"Processed: {body.decode()}"

    ch.basic_publish(
        exchange="",
        routing_key=props.reply_to,
        properties=pika.BasicProperties(correlation_id=props.correlation_id),
        body=response.encode(),
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)


connection = pika.BlockingConnection(pika.ConnectionParameters(host=RMQ_HOST, port=RMQ_PORT))
channel = connection.channel()

channel.queue_declare(queue="rpc_queue")

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="rpc_queue", on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()
