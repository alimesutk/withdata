# importing the requests library
import requests

# api-endpoint
URL = "https://jsonplaceholder.typicode.com/users"

# sending CRUD requests
r_get = requests.get(url=URL)
r_post = requests.post(url=URL)
r_patch = requests.patch(url=URL)
r_put = requests.put(url=URL)
r_delete = requests.delete(url=URL)
r_options = requests.options(url=URL)

### GET SAMPLES ###

# extracting data in json format
data = r_get.json()

#extracting id, name and email of the first matching location
id = data[0]['id']
name = data[0]['name']
email = data[0]['email']
print("ID:%s\nName:%s\nEmail:%s \n" %(id, name, email))


#list all street values with for loop
for i in data:
    print(i['address']['street'])

#list all email values with lambda for loop
[print(x['email']) for x in data]

'''
num_list = [2,3,4,5,6]
odd_num = list(map(lambda x: x%2!=0 , num_list))
print(odd_num)
'''

