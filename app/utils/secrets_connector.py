import base64
import json
import boto3
from botocore.exceptions import ClientError

AWS_REGION = "ap-southeast-2"

# 建立呼叫 AWS Secret Manager 的方法, pass 要取得的 secret_name 並 return value
def get_secret(secret_name):
  # Create a Secrets Manager client
  print("Secret Name:", secret_name)
  session = boto3.session.Session()
  client = session.client(service_name="secretsmanager", region_name=AWS_REGION)
  
  try:
    get_secret_value_response = client.get_secret_value(SecretId=secret_name)
  
  except ClientError as e:
    if e.response["Error"]["Code"] == "DecryptionFailureException":
      raise e
    elif e.response["Error"]["Code"] == "InternalServiceErrorException":
      raise e
    elif e.response["Error"]["Code"] == "InvalidParameterException":
      raise e
    elif e.response["Error"]["Code"] == "InvalidRequestException":
      raise e
    elif e.response["Error"]["Code"] == "ResourceNotFoundException":
      raise e
    print(e)

  else:
    if "SecretString" in get_secret_value_response:
      secret = get_secret_value_response["SecretString"]
    else:
      secret = base64.b64decode(get_secret_value_response["SecretBinary"])
  
  return json.loads(secret)