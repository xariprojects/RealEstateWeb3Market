# fetch_data.py
import requests

def fetch_real_estate_data(api_endpoint):
    try:
        response = requests.get(api_endpoint)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
        return response.json()
    except requests.exceptions.RequestException as e:
        print(e)
        return None

if __name__ == "__main__":
    # This API endpoint is hypothetical and would need to be replaced with a real one.
    api_endpoint = 'https://api.realestate.com/listings'
    data = fetch_real_estate_data(api_endpoint)
    
    if data:
        print("Data fetched successfully")
        # Further steps could include calling another script to publish to Pub/Sub
        # or directly importing the publish function and using it here.
