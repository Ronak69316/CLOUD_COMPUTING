#!/bin/bash
aws s3api create-bucket --bucket secure-bucket --region us-east-1
aws s3api put-bucket-policy --bucket secure-bucket --policy file://s3-bucket-policy.json
aws s3api put-bucket-encryption --bucket secure-bucket --server-side-encryption-configuration '{
    "Rules": [{
        "ApplyServerSideEncryptionByDefault": {
            "SSEAlgorithm": "aws:kms"
        }
    }]
}'