import os
import logging

APP_NAME = os.getenv("APP_NAME", "{{cookiecutter.insights_platform_app_name}}")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

logger = logging.getLogger(APP_NAME)


def log_config():
    import sys
    for k, v in sys.modules[__name__].__dict__.items():
        if k == k.upper():
            if "AWS" in k.split("_"):
                continue
            logger.info("Using %s: %s", k, v)


def get_namespace():
    try:
        with open("/var/run/secrets/kubernetes.io/serviceaccount/namespace", "r") as f:
            namespace = f.read()
        return namespace
    except EnvironmentError:
        logger.info("Not running in openshift")


# Message Queue Configuration
GROUP_ID = os.getenv("GROUP_ID", APP_NAME)
BOOTSTRAP_SERVERS = os.getenv("BOOTSTRAP_SERVERS", "kafka:29092").split(",")
CONSUME_TOPIC = os.getenv("CONSUME_TOPIC", "{{cookiecutter.insights_platform_consume_topic}}")
PRODUCE_TOPIC = os.getenv("PRODUCE_TOPIC", "{{cookiecutter.insights_platform_produce_topic}}")

# Cloudwatch Logging Configuration
AWS_ACCESS_KEY_ID = os.getenv("CW_AWS_ACCESS_KEY_ID", None)
AWS_SECRET_ACCESS_KEY = os.getenv("CW_AWS_SECRET_ACCESS_KEY", None)
AWS_REGION_NAME = os.getenv("CW_AWS_REGION_NAME", "us-east-1")
LOG_GROUP = os.getenv("LOG_GROUP", "platform-dev")

# Openshift Useful Variables
NAMESPACE = get_namespace()
BUILD_COMMIT = os.getenv("OPENSHIFT_BUILD_COMMIT", "not_in_openshift")

# Metrics for Prometheus
PROMETHEUS_PORT = int(os.getenv("PROMETHEUS_PORT", 8000))
DISABLE_PROMETHEUS = True if os.getenv("DISABLE_PROMETHEUS") == "True" else False
