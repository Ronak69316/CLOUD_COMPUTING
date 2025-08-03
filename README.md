# GCS Static Site Setup with Python

This project sets up a Google Cloud Storage bucket with:

- Static website hosting
- File uploads
- Public access
- Lifecycle rules (auto-delete after 30 days)

## Setup

1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

2. Authenticate:
    ```
    gcloud auth application-default login
    ```

3. Replace `"your-project-id"` in `gcs_setup.py` with your actual GCP Project ID.

4. Run:
    ```
    python gcs_setup.py
    ```

Enjoy your static website!
