import requests

def extract_data():
  """
  This function sends a GET request to the JSONPlaceholder API,
  retrieves the data in JSON format, and returns the extracted data.
  
  Returns:
      data (list): A list of dictionaries containing the extracted data.
  """

  url = "https://jsonplaceholder.typicode.com/users"
  response = requests.get(url)

  data = response.json()
  return data



