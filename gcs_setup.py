from google.cloud import storage
import os

# Replace with your actual Google Cloud project ID and bucket details
PROJECT_ID = "dynamic-point-467413-i0"
BUCKET_NAME = "ronak-static-site-20250729"

REGION = "us-central1"

# File(s) to upload (place your own files in the 'static' folder)
FILES_TO_UPLOAD = ["static/sample.txt"]

def setup_gcs():
    print("🔐 Initializing GCS client...")
    client = storage.Client(project=PROJECT_ID)

    print(f"📦 Creating bucket: {BUCKET_NAME} in region {REGION}...")
    bucket = client.bucket(BUCKET_NAME)
    bucket = client.create_bucket(bucket, location=REGION)
    print(f"✅ Bucket created: {bucket.name}")

    for file_path in FILES_TO_UPLOAD:
        blob_name = os.path.basename(file_path)
        print(f"⬆️ Uploading: {file_path} -> {blob_name}")
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        print(f"✅ Uploaded {blob_name} to {BUCKET_NAME}")

    # Set public read access (optional)
    print("🔓 Making files publicly accessible...")
    for file_path in FILES_TO_UPLOAD:
        blob_name = os.path.basename(file_path)
        blob = bucket.blob(blob_name)
        blob.make_public()
        print(f"🌐 Public URL: {blob.public_url}")

def main():
    setup_gcs()

if __name__ == "__main__":
    main()
