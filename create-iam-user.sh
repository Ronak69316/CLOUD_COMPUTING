#!/bin/bash
aws iam create-user --user-name SecureUser
aws iam put-user-policy --user-name SecureUser --policy-name SecurePolicy --policy-document file://iam-policy.json