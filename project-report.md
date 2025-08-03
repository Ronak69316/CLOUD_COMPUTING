# Project Report: Multi-Cloud Architecture (AWS + GCP)

## Project Title
Designing a Multi-Cloud Interoperable System using AWS and Google Cloud

## Objective
To create a microservice-oriented architecture where application components are deployed across AWS and GCP, ensuring secure communication and unified monitoring.

## Architecture
- Frontend request enters via AWS API Gateway
- Processed by AWS Lambda
- Lambda calls Google Cloud Run microservice
- Each platform independently monitors services via CloudWatch and Google Monitoring

## Key Technologies
- AWS: Lambda, API Gateway, CloudWatch
- GCP: Cloud Run, Monitoring, IAM
- Secure communication over HTTPS
- Authenticated cross-cloud API calls

## My Contribution
- Designed infrastructure on both platforms
- Wrote microservices and Lambda functions
- Enabled cross-cloud secure API communication
- Setup end-to-end monitoring and alerting

## Challenges Faced
- IAM token exchange and cross-cloud authentication
- Firewall and endpoint exposure
- Setting up alerting policies that make sense in both clouds

## Future Enhancements
- Add Azure or other platforms
- Deploy multi-region for DR
- Use service mesh for auto-routing

---

Prepared by:
Ronak Kamble
Internship Project Submission  
