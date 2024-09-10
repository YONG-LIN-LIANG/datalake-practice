import boto3
import csv
import json
from io import StringIO
from datetime import datetime

def save_to_s3(data, file_name, file_format, bucket_name, file_path, **kwargs):
  """
  This function saves the transformed data to an S3 bucket as either CSV or JSON format.
  
  Args:
      data (list): A list of dictionaries containing the transformed data.
      file_format (str): The format to save the file in ('csv' or 'json').
      bucket_name (str): The name of the S3 bucket.
      kwargs: Additional arguments such as 'execution_date'.
  """
  
  # 解析 execution_date
  execution_date = kwargs.get('execution_date')
  if execution_date:
      execution_date = datetime.strptime(execution_date, "%Y-%m-%dT%H:%M:%S.%f%z")
  else:
      execution_date = datetime.utcnow()

  # 根據 execution_date 生成時間戳
  timestamp = execution_date.strftime("%Y%m%d-%H%M%S")

  # 定義 S3 客戶端
  s3_client = boto3.client('s3')

  # 根據文件格式處理數據
  if file_format == 'csv':
    # 構建 CSV 文件名
    key = f'{file_path}{file_name}.csv'
    
    # 使用 StringIO 生成 CSV 文件
    csv_buffer = StringIO()
    writer = csv.DictWriter(csv_buffer, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
    
    # 上傳 CSV 文件到 S3
    csv_buffer.seek(0)  # 將指針重置以便讀取
    s3_client.put_object(
      Bucket=bucket_name,
      Key=key,
      Body=csv_buffer.getvalue(),
      ContentType='text/csv'
    )
    print(f"CSV file uploaded to s3://{bucket_name}/{key}")

  elif file_format == 'json':
    # 構建 JSON 文件名
    key = f'{file_path}{file_name}.json'
    
    # 上傳 JSON 文件到 S3
    s3_client.put_object(
      Bucket=bucket_name,
      Key=key,
      Body=json.dumps(data).encode('utf-8'),
      ContentType='application/json'
    )
    print(f"JSON file uploaded to s3://{bucket_name}/{key}")
      
  else:
    raise ValueError("Unsupported file format. Please choose either 'csv' or 'json'.")
