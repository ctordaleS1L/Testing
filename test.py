import requests
import json

# Define constants for the source and destination
SOURCE_URL = "https://api.source1.com/endpoint"  # Replace with the actual URL of source1
SOURCE_API_KEY = "your_source1_api_key"          # Replace with your API key for source1
SOURCE_API_SECRET = "your_source1_api_secret"    # Replace with your API secret for source1

DESTINATION_URL = "https://api.destination1.com/endpoint"  # Replace with the actual URL of destination1
DESTINATION_API_KEY = "your_destination1_api_key"          # Replace with your API key for destination1
DESTINATION_API_SECRET = "your_destination1_api_secret"    # Replace with your API secret for destination1

# Function to fetch data from source1
def fetch_data_from_source():
    headers = {
        "Authorization": f"Bearer {SOURCE_API_KEY}",  # Adjust based on the API's requirements
        "Content-Type": "application/json"
    }
    try:
        response = requests.get(SOURCE_URL, headers=headers)
        response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx
        data = response.json()  # Parse JSON data
        print("Data fetched from source1:", json.dumps(data, indent=4))
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from source1: {e}")
        return None

# Function to transform data (if required)
def transform_data(data):
    # Modify the data here if needed to match the destination1's expected format
    # Example: Convert the structure or fields
    transformed_data = {
        "key1": data.get("original_key1"),  # Map fields from source to destination
        "key2": data.get("original_key2"),
        # Add more mappings if needed
    }
    print("Transformed data:", json.dumps(transformed_data, indent=4))
    return transformed_data

# Function to save data to destination1
def save_data_to_destination(data):
    headers = {
        "Authorization": f"Bearer {DESTINATION_API_KEY}",  # Adjust based on the API's requirements
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(DESTINATION_URL, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx
        print("Data successfully saved to destination1:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error saving data to destination1: {e}")

# Main script to fetch, transform, and save data
if __name__ == "__main__":
    # Step 1: Fetch data from source1
    source_data = fetch_data_from_source()
    if source_data:
        # Step 2: Transform the data (if needed)
        transformed_data = transform_data(source_data)
        # Step 3: Save data to destination1
        save_data_to_destination(transformed_data)
