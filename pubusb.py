from google.cloud import pubsub_v1

# Create a publisher client
publisher = pubsub_v1.PublisherClient()

# Create a topic
topic_path = publisher.topic_path("<project-id>", "<topic-name>")
topic = publisher.create_topic(request={"name": topic_path})
print(f"Topic created: {topic.name}")

# Publish a message
message = "Hello, Pub/Sub!"
data = message.encode("utf-8")
future = publisher.publish(topic_path, data)
print(f"Published message: {message}")

# Create a subscriber client
subscriber = pubsub_v1.SubscriberClient()

# Create a subscription
subscription_path = subscriber.subscription_path("<project-id>", "<subscription-name>")
subscription = subscriber.create_subscription(request={"name": subscription_path, "topic": topic_path})
print(f"Subscription created: {subscription.name}")

# Define a callback function to handle received messages
def callback(message):
    print(f"Received message: {message.data.decode('utf-8')}")
    message.ack()

# Start the subscriber
subscriber.subscribe(subscription_path, callback=callback)

# Keep the script running to continuously receive messages
while True:
    pass

