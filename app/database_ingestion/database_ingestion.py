from utils.tasks import BaseTask
from utils.s3_connector import S3Connector
from utils.postgresql_connector import PostgresqlConnector
import yaml
import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd
import io
from datetime import datetime

# DataIngestionTask 類別 繼承 BaseTask 類別
class DataIngestionTask(BaseTask):
  def __init__(
    self, 
    task_name: str, 
    config_path: str = None,
  ):
    # 手動呼叫父類別 (BaseTask) 的 __init__ 
    # super().__init__(task_name)
    BaseTask.__init__(self, task_name)
    self.config_path = config_path
    # 定義 s3_con 為 S3Connector 實體
    self.s3_con = S3Connector()
    
    
    # 宣告 ingestion_config 來讀取 yaml config
    self.ingestion_config = self.read_config_yaml_file()
    # 取得 yaml config 的 pipeline_config
    self.pipeline_config = self.ingestion_config.get('pipeline_config')

    self.ingestion_table_list = self.pipeline_config['ingestion_table_list']
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
    if len(self.ingestion_table_list) == 0:
      for table in self.ingestion_config.get('tables'):
        table_config_list.append(table)
    else:
      for table_to_check in self.ingestion_table_list:
        for table in self.ingestion_config.get('tables'):
          for name, config in table.items():
            if name == table_to_check:
              table_config_list.append(table)
    return table_config_list

  def write_table_to_pq():
    df = pd.read_sql("SELECT * FROM your_table", your_db_connection)
    # 將 DataFrame 轉換為 Parquet 文件
    table = pa.Table.from_pandas(df)
    pq.write_table(table, 'your_table.parquet')

  def fetch_data_from_postgres(self, table_name, day_load_duration, extract_column_list):
    connection = self.source_db_connection
    cursor = connection.cursor()
    columns = ",".join(extract_column_list)
    query = f"SELECT {columns} FROM {table_name} WHERE updated_at >= CURRENT_DATE - INTERVAL {day_load_duration};"
    cursor.execute(query)
    records = cursor.fetchall()

    # Get column names
    column_names = [desc[0] for desc in cursor.description]

    # Convert result to a list of dictionaries
    result = [dict(zip(column_names, record)) for record in records]

    return result
  
  def run_pipeline(self):
    # 取得要上傳的 for loop 所有Table
    for table in self.get_table_config_list():
      table_name = list(table.keys())[0]
      s3_file_path = table['s3_file_path']
      current_timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
      export_file_name = f"{current_timestamp}.parquet"
      day_load_duration = table['day_load_duration']
      extract_column_list = table['column_to_extract']
      table_data = self.fetch_data_from_postgres(table_name, day_load_duration, extract_column_list)
      df = pd.DataFrame(table_data)
      output_file = f"s3://{self.bucket_name}/{s3_file_path}/{export_file_name}"
      df.to_parquet(output_file)

    print('Task Finished!')


    
    

    
    

    
    