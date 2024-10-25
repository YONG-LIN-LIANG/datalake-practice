from utils.tasks import BaseTask
from utils.s3_connector import S3Connector
from utils.postgresql_connector import PostgresqlConnector
import yaml
import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd
import io

# DataIngestionTask 類別 繼承 BaseTask 類別
class DataIngestionTask(BaseTask):
  def __init__(
    self, 
    task_name: str, 
    config_path: str = None,
    table_name: str = None
  ):
    print("check", config_path)
    # 手動呼叫父類別 (BaseTask) 的 __init__ 
    # super().__init__(task_name)
    BaseTask.__init__(self, task_name)
    self.config_path = config_path
    # 定義 s3_con 為 S3Connector 實體
    self.s3_con = S3Connector()
    self.table_name = table_name
    
    # 宣告 ingestion_config 來讀取 yaml config
    self.ingestion_config = self.read_config_yaml_file()
    # 取得 yaml config 的 pipeline_config
    self.pipeline_config = self.ingestion_config.get('pipeline_config')
    # Connect Local PostgreSQL
    self.source_db_connection = PostgresqlConnector(
      secret_name=self.pipeline_config['source_credentials']
    ).get_connection()
    self.bucket_name = self.pipeline_config['s3_bucket_name']

  # 讀取 yaml 檔內容
  def read_config_yaml_file(self) -> dict:
    # config_path 為 config yaml 路徑
    with open(self.config_path, 'r') as f:
      # 將 YAML 格式的數據轉換成 Python 資料結構（如字典、列表等）
      return yaml.full_load(f)

   # 拿取 configuration
  def get_table_config_list(self) -> list:
    table_config_list = []
    if self.table_name is None:
      for table in self.ingestion_config.get('tables'):
        table_config_list.append(table)
    else:
      for table in self.ingestion_config.get('tables'):
        for name, config in table.items():
          if name == self.table_name:
            table_config_list.append(table)
    return table_config_list

  def write_table_to_pq():
    df = pd.read_sql("SELECT * FROM your_table", your_db_connection)
    # 將 DataFrame 轉換為 Parquet 文件
    table = pa.Table.from_pandas(df)
    pq.write_table(table, 'your_table.parquet')

  def fetch_data_from_postgres(self, table_name):
    connection = self.source_db_connection
    cursor = connection.cursor()
    query = f'SELECT * FROM {table_name}'
    cursor.execute(query)
    records = cursor.fetchall()

    # Get column names
    column_names = [desc[0] for desc in cursor.description]

    # Convert result to a list of dictionaries
    result = [dict(zip(column_names, record)) for record in records]

    return result

  def export_to_parquet(self, data):
    # 將數據轉換為 DataFrame
    df = pd.DataFrame(data)
    table = pa.Table.from_pandas(df)

    # 創建一個內存buffer
    buffer = io.BytesIO()
    
    # 將數據寫入buffer，格式為parquet
    pq.write_table(table, buffer)
    buffer.seek(0)

    return buffer

  
  
  def run_pipeline(self):
    # 取得要上傳的 for loop 所有Table
    for table in self.get_table_config_list():
      table_name = list(table.keys())[0]
      s3_file_path = table['s3_file_path']
      export_file_name = table['export_file_name']
      table_data = self.fetch_data_from_postgres(table_name)
      buffer = self.export_to_parquet(table_data)
      self.s3_con.upload_file(buffer, self.bucket_name, f'{s3_file_path}/{export_file_name}')

    print('Task Finished!')


    
    

    
    

    
    