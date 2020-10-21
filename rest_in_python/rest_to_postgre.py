# Import libraries
import requests #http request library
import psycopg2 #postgre connection library
import secrets #project secrets file

# Connecting to PostgreDB
connection = psycopg2.connect(user = secrets.pg_user, password = secrets.pg_password,
                              host = "127.0.0.1", port = "5432", database = "postgres")
cursor = connection.cursor()

# API-Endpoint
URL = "https://jsonplaceholder.typicode.com/albums"

# Sending GET request
r_get = requests.get(url=URL)

# Extracting data in JSON format
data = r_get.json()

# Write JSON data to PostgreDB table
for p in data:
    userId = p['userId']
    id = p['id']
    title = p['title']
    #print(str(userId) + '\t' + str(id) + '\t' + str(title))
    cursor.execute("INSERT INTO typicode.albums (userid, id, title) VALUES ('%d','%d','%s')" %(userId,id,title))
    connection.commit()
cursor.close()
connection.close()
