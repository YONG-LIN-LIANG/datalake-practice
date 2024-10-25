from database_ingestion.database_ingestion import DataIngestionTask
import os

def execute():
  # Execute "DataIngestionTask" Task
  # 執行 postgresql 的 pipeline
  task = DataIngestionTask(
    'DataIngestionTask', 
    os.path.join(os.path.dirname(__file__), 'database_ingestion/config/proj_crm.yml')
  )

  task.run_pipeline()




if __name__ == '__main__':
  execute()