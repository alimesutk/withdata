# importing the requests library
import requests

# api-endpoint
URL = "https://jsonplaceholder.typicode.com/users"

# location given here
location = "delhi technological university"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'address': location}

# sending get request and saving the response as response object
r = requests.get(url=URL)

# extracting data in json format
data = r.json()

# extracting latitude, longitude and formatted address
# of the first matching location
id = data[0]['id']
name = data[0]['name']
email = data[0]['email']

# printing the output
print("ID:%s\nName:%s\nEmail:%s"
      % (id, name, email))
