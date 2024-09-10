def transform_data(data):
  """
  This function takes the raw data extracted from the API and applies
  some transformations to make it more suitable for further analysis or storage.
  
  Args:
      data (list): A list of dictionaries containing the raw data.
      
  Returns:
      transformed_data (list): A list of dictionaries containing the transformed data.
  """

  # data = ti.xcom_pull(task_ids="extract_data")

  transformed_data = []

  for record in data:
    transformed_record = {
      'id': record['id'],
      'name': record['name'],
      'username': record['username'],
      'email': record['email'],
      'address': record['address']['street'] + ', ' + record['address']['city'] + ', ' + record['address']['zipcode']
    }
    transformed_data.append(transformed_record)

  return transformed_data