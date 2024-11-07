import boto3
from botocore.exceptions import NoCredentialsError, ClientError
import logging
import os

# Configuration - using environment variables for security
ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
LOCAL_FILE = "local_file_name"
BUCKET_NAME = "bucket_name"
S3_FILE_NAME = "file_name_on_s3"

def create_s3_client():
    """Create and return an S3 client using AWS credentials."""
    try:
        s3 = boto3.client(
            "s3", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY
        )
        return s3
    except NoCredentialsError:
        logging.error("Credentials not found. Please check your AWS credentials.")
        return None

def upload_to_s3(local_file, bucket, s3_file):
    """
    Upload a file to an S3 bucket.
    
    Parameters:
    - local_file: Path to the local file to be uploaded
    - bucket: Target S3 bucket name
    - s3_file: Desired S3 file path/name
    
    Returns:
    - True if the file was uploaded, False otherwise
    """
    s3 = create_s3_client()
    if s3 is None:
        return False

    try:
        s3.upload_file(local_file, bucket, s3_file)
        logging.info(f"File '{local_file}' uploaded to '{bucket}/{s3_file}' successfully.")
        return True
    except FileNotFoundError:
        logging.error(f"The file '{local_file}' was not found.")
        return False
    except NoCredentialsError:
        logging.error("Credentials not available.")
        return False
    except ClientError as e:
        logging.error(f"Failed to upload file due to: {e}")
        return False

# Configure logging
logging.basicConfig(level=logging.INFO)

# Run the upload function
if __name__ == "__main__":
    result = upload_to_s3(LOCAL_FILE, BUCKET_NAME, S3_FILE_NAME)
