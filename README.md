# AWS Lambda Function for CSV to JSON Conversion

This repository contains Terraform configuration files to set up an AWS Lambda function that converts CSV files to JSON. The Lambda function is triggered by an S3 event notification whenever a new CSV file is uploaded to a specified S3 bucket.

## Prerequisites

- [Terraform](https://www.terraform.io/downloads.html) installed.
- AWS account with credentials configured locally (`aws configure`).

## Configuration Overview

1. **S3 Bucket**: An S3 bucket is created to store CSV files. When a new CSV file is uploaded, it triggers the Lambda function.
2. **IAM Role and Policies**: An IAM role with the necessary permissions is created for the Lambda function to interact with S3.
3. **Lambda Function**: A Lambda function written in Python is provided. It reads a CSV file from the S3 bucket, converts it to JSON, and writes the JSON back to the same bucket.
4. **S3 Bucket Notification**: The S3 bucket is configured to trigger the Lambda function on object creation events, specifically when new CSV files are uploaded.

