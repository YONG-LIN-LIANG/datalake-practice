import os
import sys
import json
import csv
import boto3
import psycopg2

parent_directory = os.path.abspath('..')
sys.path.append(parent_directory)

from save_to_s3 import save_to_s3


# Connect to PostgreSQL
def fetch_data_from_postgres(table_name):
  connection = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    port="5433",
    user="admin",
    password="root"
  )
  cursor = connection.cursor()
  query = f'SELECT * FROM {table_name}'
  cursor.execute(query)
  records = cursor.fetchall()

  # 獲取列名稱
  column_names = [desc[0] for desc in cursor.description]

  # 將結果轉換為列表的字典形式
  result = [dict(zip(column_names, record)) for record in records]

  # 關閉連接
  cursor.close()
  connection.close()

  return result


# 將數據轉換為 CSV 並上傳到 S3
# def write_csv_to_s3(data, bucket_name, file_name):
#   csv_buffer = StringIO()
#   writer = csv.DictWriter(csv_buffer, fieldnames=data[0].keys())
#   writer.writeheader()
#   writer.writerows(data)

#   csv_buffer.seek(0)  # 將指針重置以便讀取

#   s3_client = boto3.client('s3')

#   # 將 CSV 文件上傳到 S3
#   s3_client.put_object(
#     Bucket=bucket_name,
#     Key=file_name,
#     Body=csv_buffer.getvalue(),
#     ContentType='text/csv'
#   )

#   print(f'Successfully uploaded {file_name} to {bucket_name} as CSV.')




if __name__ == '__main__':
  tables = ['customers', 'orders', 'products', 'order_items']
  bucket_name = 'datalakepractice'
  file_format = 'csv'
  file_path = 'data/business/'
  for table in tables:
    # Step 1: Fetch data from postgresql
    data = fetch_data_from_postgres(table)
    file_name = f'{table}'
    save_to_s3(data, file_name, file_format, bucket_name, file_path)
  

