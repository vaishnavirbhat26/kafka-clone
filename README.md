# kafka-clone
A simplified Python program that demonstrates some of the core functionalities, such as topic creation, message publishing, and basic consumer simulation. 

Output:
<img width="467" alt="image" src="https://github.com/vaishnavirbhat26/kafka-clone/assets/112920991/4b0723d8-1476-4791-8845-1f71db6ad381">


In this simplified example:

1. We have a create_topic function to create new topics, a publish_message function to publish messages to topics, and a basic consumer function to simulate consumers.
2. We simulate the creation of two topics, "topic1" and "topic2."
3. We simulate the publishing of messages to these topics.
4. We simulate two consumer threads (consumer1 and consumer2) that continuously check for messages in their respective topics.
5. The main program continues to publish messages to topics to observe how consumers receive them.

Please note that this is a basic simulation, and a real message broker system like Kafka would involve more advanced features, such as distributed message storage, message replication, partitioning, and advanced consumer group management. This example provides a starting point for understanding the core concepts of message brokers.
