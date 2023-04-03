import socket
import mysql.connector

#Connect to MariaDB database
cnx = mysql.connector.connect(
    user='your-username',
    password='your-password',
    host='your-hostname',
    database='your-database')

cursor = cnx.cursor()

# Create a socket for machine 1
sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock1.connect(('machine1_ip', 'machine1_port'))

# Create a socket for machine 2
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2.connect(('machine2_ip', 'machine2_port'))

# Send a query to the machines
query = str(input('Enter the query:'))
sock1.sendall(query.encode())
sock2.sendall(query.encode())

#Execute query
cursor.execute(query)
result = cursor.fetchall()


# Receive the results from machine 1
result1 = sock1.recv(1024).decode()

# Receive the results from machine 2
result2 = sock2.recv(1024).decode()

# Combine the results from all machines
final_results = result + result1 + result2

# Print results
for result in final_results:
    print(result)

phf_query= "CREATE TABLE students_campus1 AS SELECT * FROM students WHERE campus_id = 1 OR campus_id =2; CREATE TABLE students_campus2 AS SELECT * FROM students WHERE campus_id = 3 OR campus_id =4;CREATE TABLE students_campus3 AS SELECT * FROM students WHERE campus_id = 5;"