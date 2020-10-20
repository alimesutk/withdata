# importing the libraries
import requests #http request library
import psycopg2 #postgre connection library
import secrets

# connecting postgre
connection = psycopg2.connect(user = secrets.pg_user, password = secrets.pg_password,
                              host = "127.0.0.1", port = "5432", database = "postgres")
cursor = connection.cursor()

# api-endpoint
URL = "https://jsonplaceholder.typicode.com/albums"

# sending CRUD requests
r_get = requests.get(url=URL)

# extracting data in json format
data = r_get.json()

#extracting userId, id and title of the first matching location


#
for p in data:
    userId = p['userId']
    id = p['id']
    title = p['title']
    print(str(userId) + '\t' + str(id) + '\t' + str(title))
    cursor.execute("INSERT INTO typicode.albums (userid, id, title) VALUES ('%d','%d','%s')" %(userId,id,title))
    connection.commit()
cursor.close()
connection.close()

'''
result=cursor.execute("INSERT INTO public.xml_food VALUES (3,'%s')" %resp)
connection.commit()



#list all street values with for loop
for i in data:
    print(i['title'])

#list all email values with lambda for loop
[print(x['title']) for x in data]

for i in data:
    print(i['title'])



num_list = [2,3,4,5,6]
odd_num = list(map(lambda x: x%2!=0 , num_list))
print(odd_num)
'''

