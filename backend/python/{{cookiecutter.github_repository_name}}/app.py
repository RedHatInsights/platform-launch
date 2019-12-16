import traceback

from prometheus_client import start_http_server
from kafka.errors import KafkaError

from utils import config, metrics, log
from mq import consume, produce

logger = log.initialize_logging()


def start_prometheus():
    start_http_server(config.PROMETHEUS_PORT)


producer = None


def main():
    """Creates the main loop where messages are read from the consume queue.
    Also initializes logging and sets up prometheus if configured.
    """

    logger.info(f"Starting {config.APP_NAME} Service")

    config.log_config()

    if not config.DISABLE_PROMETHEUS:
        logger.info(f"Starting {config.APP_NAME} Prometheus Server")
        start_prometheus()

    consumer = consume.init_consumer()
    global producer
    producer = produce.init_producer()

    while True:
        for data in consumer:
            try:
                handle_message(data.value)
            except Exception:
                logger.exception("An error occurred during message processing")

        producer.flush()


def send_message(topic, msg):
    """Helper function to send a message to a topic via the established produce
    queue.

    Arguments:
        topic string -- The topic to produce to
        msg dict -- The dictionary that needs to be sent on the mq
    """
    try:
        producer.send(topic, value=msg)
        logger.debug("Message sent to [%s] topic for id [%s]", topic)
    except KafkaError:
        logger.exception("Failed to produce message to [%s] topic: %s", topic)
        metrics.msg_send_failure.inc()
    metrics.msg_sent.inc()


def handle_message(msg):
    """Handles the incoming message you receive from the message queue.
    
    Arguments:
        msg dict -- dictionary of the message
    """
    metrics.msg_count.inc()
    logger.info(msg)
    # Fill in with functions or actions to take on the message
    


if __name__ == "__main__":
    try:
        main()
    except Exception:
        the_error = traceback.format_exc()
        logger.error(f"{config.APP_NAME} failed with Error: {the_error}")
