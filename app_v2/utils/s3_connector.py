import boto3
from botocore.exceptions import ClientError

class S3Connector:
  def __init__(self):
    self.configure()
  # 設置 S3 服務連接
  def configure(self):
    # Connect 
    try:
      # Credential(secret key...etc) stored in the local device, here we just need to define service name that we are connecting to.
      # boto3.client 和 boto3.resource 都是對 s3 儲存桶進行操作，選一種就行
      self.s3_client = boto3.client('s3')
      self.s3_resource = boto3.resource('s3')
    except ClientError as e:
        print(f"ClientError occurred: {e}")
        # 獲取錯誤代碼
        error_code = e.response['Error']['Code']
        # 根據錯誤代碼進行處理
        if error_code == 'AccessDenied':
            print("Access denied: Check your AWS credentials and permissions.")
        elif error_code == 'InvalidClientTokenId':
            print("Invalid AWS token: Check your AWS credentials.")
        else:
            print(f"Unexpected error: {e}")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

  def list_bucket(self):
     # 列出所有 S3 存儲桶
    try:
      response = self.s3_client.list_buckets()
      buckets = [bucket["Name"] for bucket in response["Buckets"]]
      print(buckets)
    except ClientError as e:
      print(f"ClientError occurred while listing buckets: {e}")
      error_code = e.response['Error']['Code']
      # 根據錯誤代碼進行處理
      if error_code == 'AccessDenied':
          print("Access denied: Unable to list buckets.")
      else:
          print(f"Unexpected error: {e}")
    except Exception as e:
      print(f"An error occurred: {e}")

  def upload_file(self, buffer, bucket_name, file_path):
    try:
        if self.s3_client is None:
            raise ValueError("S3 client not configured. Call configure() first.")
        self.s3_client.upload_fileobj(buffer, bucket_name, file_path)
    except ClientError as e:
        print(f"Error uploading file to S3: {str(e)}")
        raise
    except Exception as e:
        print(f"Unexpected error during upload: {str(e)}")
        raise