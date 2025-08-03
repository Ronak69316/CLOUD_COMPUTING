#!/bin/bash
aws cloudwatch put-metric-alarm --alarm-name "HighCPUAlarm" \
  --metric-name "CPUUtilization" --namespace "AWS/EC2" --statistic "Average" \
  --period 300 --threshold 70 --comparison-operator "GreaterThanThreshold" \
  --dimensions Name=InstanceId,Value=i-REPLACE_WITH_YOUR_INSTANCE_ID \
  --evaluation-periods 1 --alarm-actions arn:aws:sns:REGION:ACCOUNT_ID:YourTopic \
  --unit "Percent"
