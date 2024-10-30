# Trip Data Downloader - GCP Cloud Function (2nd Gen)

This Google Cloud Function downloads monthly NYC Yellow Taxi trip data files from a public NYC URL and uploads them to a Google Cloud Storage bucket. It iterates through dates from January 2009 to August 2024, constructing the URL for each file, downloading it, and storing it in the specified bucket.

## Function Overview

- **Source URL Pattern**: `https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_<YYYY-MM>.parquet`
- **Date Range**: January 2009 to August 2024
- **Destination**: Google Cloud Storage bucket of your choice

## Deployment Instructions

1. **Prepare Function Files**:
   - `main.py`: Contains the function code.
   - `requirements.txt`: Lists dependencies for `google-cloud-storage` and `requests`.

2. **Deploy the Function**:

   Use the `gcloud` CLI to deploy the function as a 2nd Generation Cloud Function in `us-central1`:

   ```sh
   gcloud functions deploy download-trip-data-v3 \
       --gen2 \
       --runtime python310 \
       --region us-central1 \
       --entry-point download_and_upload_data \
       --trigger-http \
       --allow-unauthenticated \
       --memory=16Gi \
       --cpu=4

3. **Triggering the Function**:

    Once deployed, the function can be triggered by sending an HTTP POST request to the generated URL. You can trigger it using `curl`:
    ```sh
    curl -X POST https://us-central1-PROJECT_ID.a.run.app

