import boto3
import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def upload_file_to_s3(file_path: str, bucket_name: str, s3_key: str):
    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"{file_path} not found.")

    logger.info(f"Preparing to upload {file_path} to s3://{bucket_name}/{s3_key}")

    try:
        s3_client = boto3.client('s3')
        s3_client.upload_file(file_path, bucket_name, s3_key)
        logger.info(f"Successfully uploaded {file_path} to s3://{bucket_name}/{s3_key}")
    except Exception as e:
        logger.error(f"Failed to upload {file_path} to S3: {e}")
        raise
    
