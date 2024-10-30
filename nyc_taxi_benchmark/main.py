import datetime
import requests
from google.cloud import storage

# Set up your bucket name
BUCKET_NAME = '<bucket_name>'

def download_and_upload_data(request):
    # Initialize Google Cloud Storage client
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(BUCKET_NAME)

    # Date range to iterate over
    start_date = datetime.date(2009, 1, 1)
    end_date = datetime.date(2024, 8, 1)

    current_date = start_date

    while current_date <= end_date:
        # Construct the URL
        date_str = current_date.strftime("%Y-%m")
        url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{date_str}.parquet"
        blob_name = f"yellow_tripdata_{date_str}.parquet"

        # Attempt to download the file
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()  # Check if the download was successful
            blob = bucket.blob(blob_name)
            blob.upload_from_string(response.content)

            print(f"Uploaded {blob_name} to {BUCKET_NAME}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download {blob_name}: {e}")

        # Move to the next month
        next_month = current_date.month % 12 + 1
        next_year = current_date.year + (current_date.month + 1 > 12)
        current_date = datetime.date(next_year, next_month, 1)

    return "Download and upload process completed."

