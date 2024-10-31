import psycopg2
import pandas as pd
from utils.secrets_connector import get_secret

# 連接 Postgresql
class PostgresqlConnector:
  # secret_name 的內容記錄在 config 資料夾裡的 yaml 設定檔
  def __init__(self, secret_name):
    self.secret_name = secret_name
    self.credentials = get_secret(self.secret_name)
  
  def get_connection(self):
    try:
      # host, dbname, port, user, password 存放在 Secret Manager 裡
      connection = psycopg2.connect(
        host=self.credentials.get('host'),
        database=self.credentials.get('database'),
        port=self.credentials.get('port'),
        user=self.credentials.get('user'),
        password=self.credentials.get('password')
      )

    except Exception as e:
      print(e)
      raise e
    
    return connection