# Baseline Python Platform App

This directory provies the necessary files for a bare bones application that can
communicate with platform services via the message queue.

At a minimum, a configuration for the consuming topic and production topic must 
be provided. If you choose to only read, you can safely remove the produce topic 
messages.

Logging is also provided in the base app. To log to cloudwatch you'll need AWS 
key credentials with access to the log group configured for your app. Many of these
required components can be assigned via environment variable as that's the way they
will work once in openshift.

To test your app, you can stand up a local Kafka and Zookeeper instance and connect
to it that way.

# Simple Kafka deployment

    podman pod create --name kafka -p 29092:29092
    
    podman run -d --pod kafka --name zookeeper -e ZOOKEEPER_CLIENT_PORT=32181 -e ZOOKEEPER_SERVER_ID=1 confluentinc/cp-zookeeper 
    
    podman run -d --pod kafka --name kafka1 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:29092 -e KAFKA_BROKER_ID=1 -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 -e KAFKA_ZOOKEEPER_CONNECT=localhost:32181 confluentinc/cp-kafka

# Run the app

    virtualenv .
    source bin/activate
    pip install -r requirements.txt
    python app.py
