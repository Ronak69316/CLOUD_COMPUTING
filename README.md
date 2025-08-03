# Multi-Cloud Architecture with Interoperable Services (AWS + GCP)

This project showcases a multi-cloud architecture where services are distributed across **AWS** and **Google Cloud Platform (GCP)** with interoperability between the two platforms.

---

## 🎯 Objectives

- Build services across both AWS and GCP
- Enable communication between services using secure APIs
- Demonstrate monitoring and alerting in a multi-cloud environment

---

## 🏗️ Architecture Overview

```
                        ┌────────────────────┐
                        │   Client (Browser) │
                        └─────────┬──────────┘
                                  │
                        ┌─────────▼─────────────┐
                        │ API Gateway (AWS)     │
                        └─────────┬─────────────┘
                                  │
                        ┌─────────▼───────────────┐
                        │ Lambda (AWS)            │
                        │ - Sends requests to     │
                        │   GCP service endpoint  │
                        └─────────┬───────────────┘
                                  │
                        ┌─────────▼──────────────┐
                        │ Cloud Run (GCP)        │
                        │ - Microservice endpoint│
                        │ - Handles requests     │
                        └─────────┬──────────────┘
                                  │
                        ┌─────────▼─────────────┐
                        │ Monitoring (CloudWatch│
                        │ + GCP Monitoring)     │
                        └───────────────────────┘
```

---

## 🧱 Components

### AWS
- API Gateway (REST endpoint)
- Lambda (invokes GCP service)
- CloudWatch (monitoring)
- IAM Roles

### GCP
- Cloud Run (microservice endpoint)
- Google Monitoring
- Cloud IAM & APIs

---

## 🔧 Interoperability

1. **API Gateway** receives request and triggers **Lambda**.
2. **Lambda** sends authenticated HTTPS request to **GCP Cloud Run** using a service account or token.
3. Cloud Run processes the request and returns a response.
4. Both platforms log and monitor independently and send alerts.

---

## 🔐 Security
- HTTPS communication only
- Use IAM or OAuth 2.0 for authentication between AWS Lambda and GCP Cloud Run
- Principle of least privilege on roles/policies

---

## 🚀 Setup Instructions

1. Deploy API Gateway and Lambda using AWS CLI or CloudFormation.
2. Deploy Cloud Run service using GCP CLI (`gcloud`) or YAML.
3. Set up metrics and alerts in both AWS CloudWatch and GCP Monitoring.
4. Test endpoint from browser or CLI.

---

## 🧪 Demo

- Make a request to AWS API Gateway endpoint:
  ```
  curl https://your-api-id.execute-api.region.amazonaws.com/prod/
  ```
- Verify Cloud Run logs via:
  ```
  gcloud logging read "resource.type=cloud_run_revision"
  ```

---

## 📁 Structure

```
multi-cloud-architecture/
├── aws/
│   ├── lambda-handler.js
│   ├── cloudformation.yaml
│   └── README.md
├── gcp/
│   ├── main.py
│   ├── cloudrun.yaml
│   └── README.md
├── README.md
└── project-report.md
```
