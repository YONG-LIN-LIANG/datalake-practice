import json
import boto3
import time

glue_client = boto3.client('glue')

def lambda_handler(event, context):
  # TODO implement

  while True:
      state = glue_client.get_crawler(Name='business')['Crawler']['State']
      if state == 'READY':
          break
      print(f"The Crawler 'business' is not ready yet; current state: {state}")
      time.sleep(5)

  print(f'The Crawler business is Ready lol')
  response = glue_client.start_crawler(
      Name = 'business'
  )

  return {
      'statusCode': 200,
      'body': json.dumps('Hello from Lambda haaha!')
  }
