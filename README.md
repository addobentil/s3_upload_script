# S3 File Upload Script

This script uploads a specified local file to an AWS S3 bucket. It’s designed to securely manage AWS credentials and provides detailed logging for easier troubleshooting.

## Features

- **Secure Credential Management**: Uses environment variables to store AWS credentials securely.
- **Error Handling**: Captures and logs common errors, such as missing credentials, file not found, and client errors.
- **Modular Design**: The S3 client setup is separated into a reusable function.

## Prerequisites

- **Python 3.x**
- **boto3 library** (Install with `pip install boto3`)
- **AWS Account** with access to S3
- **AWS Credentials** (Access Key ID and Secret Access Key)

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/addobentil/s3_upload_script.git
   ```

2. Navigate to the project directory:

```bash
cd s3_upload_script
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```
