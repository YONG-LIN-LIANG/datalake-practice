import os
import sys
from extract_data import extract_data
from transform_data import transform_data
parent_directory = os.path.abspath('..')
sys.path.append(parent_directory)
from save_to_s3 import save_to_s3

if __name__ == '__main__':
  # Extract Data
  data = extract_data()
  # Transform Data
  transformed_data = transform_data(data)
  # Load Data
  save_to_s3(
    transformed_data,
    'user_list',  # file_name
    'json',  # file_format
    'datalakepractice',  # bucket_name
    'data/users/'  # file_path
  )
