# importing the requests library
import requests
import pandas as pd

# api-endpoint
URL = "https://jsonplaceholder.typicode.com/users"

# sending get request and saving the response as response object
r = requests.get(url=URL)
p = requests.post(url=URL)

# extracting data in json format
data = r.json()
pdj=pd.read_json(r)
print(pdj)
