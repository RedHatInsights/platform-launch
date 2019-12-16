from prometheus_client import Summary, Counter
from utils import config

APP_NAME = config.APP_NAME.replace("-", "_")

msg_count = Counter(f"{APP_NAME}_messages_consumed_total", "Total messages consumed from the kafka topic")
msg_sent = Counter(f"{APP_NAME}_messages_sent_total", "Total messages successfully sent")
msg_send_failure = Counter(f"{APP_NAME}_messages_failed_to_send_total", "Total messages that failed to send")
