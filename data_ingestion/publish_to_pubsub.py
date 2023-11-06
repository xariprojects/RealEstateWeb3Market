# publish_to_pubsub.py
from google.cloud import pubsub_v1
import json

# Assumes you have set up Google Cloud credentials in the environment
publisher = pubsub_v1.PublisherClient()
project_id = "your-gcp-project-id"
topic_id = "real-estate-topic"

topic_path = publisher.topic_path(project_id, topic_id)

def publish_to_pubsub(data):
    data_json = json.dumps(data)
    data_bytes = data_json.encode("utf-8")

    try:
        publish_future = publisher.publish(topic_path, data=data_bytes)
        publish_future.result()  # Verify the publish succeeded
        print(f"Data published to {topic_path}.")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    # This would be replaced with the actual data fetched from the API
    mock_data = {"id": "123", "price": 300000, "location": "Downtown"}
    publish_to_pubsub(mock_data)
