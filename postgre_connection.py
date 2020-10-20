import psycopg2
from rest_in_python import secrets

connection = psycopg2.connect(user = secrets.pg_user, password = secrets.pg_password,
                              host = "127.0.0.1", port = "5432", database = "postgres")
cursor = connection.cursor()
# Print PostgreSQL Connection properties
print ( connection.get_dsn_parameters(),"\n")
# Print PostgreSQL version
cursor.execute("SELECT * FROM typicode.albums")
record = cursor.fetchone()
print("You are connected to - ", record,"\n")

cursor.close()
connection.close()