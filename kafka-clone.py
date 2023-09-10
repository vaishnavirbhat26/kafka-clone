import threading
import time

# Global variables to simulate message storage and topics
message_storage = {}
topics = {}


# Function to create a new topic
def create_topic(topic_name):
    if topic_name not in topics:
        topics[topic_name] = []


# Function to publish a message to a topic
def publish_message(topic_name, message):
    if topic_name in topics:
        topics[topic_name].append(message)
    else:
        print(f"Topic '{topic_name}' does not exist.")


# Function to simulate a consumer
def consumer(topic_name, consumer_id):
    while True:
        if topic_name in topics and topics[topic_name]:
            message = topics[topic_name].pop(0)
            print(f"Consumer-{consumer_id} received message from '{topic_name}': {message}")
        time.sleep(1)


# Simulate topic creation
create_topic("topic1")
create_topic("topic2")

# Simulate message publishing
publish_message("topic1", "Message 1 for topic1")
publish_message("topic1", "Message 2 for topic1")
publish_message("topic2", "Message 1 for topic2")

# Simulate consumers
consumer1 = threading.Thread(target=consumer, args=("topic1", 1))
consumer2 = threading.Thread(target=consumer, args=("topic2", 2))

consumer1.start()
consumer2.start()

# Main program continues to simulate message publishing
publish_message("topic2", "Message 2 for topic2")

# Wait for consumers to finish (in a real system, consumers would run indefinitely)
consumer1.join()
consumer2.join()
