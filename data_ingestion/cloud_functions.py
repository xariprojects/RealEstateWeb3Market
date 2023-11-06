# cloud_function.py
from google.cloud import bigquery
import base64
import json

def ingest_to_bigquery(event, context):
    """Background Cloud Function to be triggered by Pub/Sub.
    Args:
         event (dict): The dictionary with data specific to this type of event.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    data = json.loads(pubsub_message)

    # Initialize a BigQuery client
    client = bigquery.Client()
    dataset_id = 'your_bigquery_dataset_id'
    table_id = 'your_bigquery_table_id'
    
    # Prepare a BigQuery insert
    table_ref = client.dataset(dataset_id).table(table_id)
    table = client.get_table(table_ref)

    # Insert the data into the BigQuery table
    errors = client.insert_rows_json(table, [data])
    if errors:
        raise RuntimeError(f"Data insertion failed: {errors}")

# The function can be deployed to GCP Cloud Functions with the necessary triggers and environment variables.
