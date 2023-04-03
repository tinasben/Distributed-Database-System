import psycopg2
import socket

# Connect to the PostgreSQL database
pg_config = {
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'database': 'school'
}

pg_conn = psycopg2.connect(**pg_config)
pg_cursor = pg_conn.cursor()

pg_query = "SELECT * FROM students_campus1;"
phf_query= "CREATE TABLE students_campus1 AS SELECT * FROM students WHERE campus_id = 1 OR campus_id =2; CREATE TABLE students_campus2 AS SELECT * FROM students WHERE campus_id = 3 OR campus_id =4;CREATE TABLE students_campus3 AS SELECT * FROM students WHERE campus_id = 5;"
dhf_query= "CREATE TABLE hostels_west  AS SELECT * FROM hostels WHERE campus_id IN (SELECT campus_id FROM campuses WHERE region = 'West'); CREATE TABLE hostels_north  AS SELECT * FROM hostels WHERE campus_id IN (SELECT campus_id FROM campuses WHERE region = 'North'); CREATE TABLE hostels_south  AS SELECT * FROM hostels WHERE campus_id IN (SELECT campus_id FROM campuses WHERE region = 'South');"
vf_query= ""
pg_cursor.execute(phf_query)
pg_conn.commit()
pg_cursor.execute(pg_query)

pg_results = pg_cursor.fetchall()
print(pg_results)

# Create a socket for connecting to the main machine
# sockmain = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sockmain.connect(('machine1_ip', 'machine1_port'))

# # Receive the query from main machine
# query = sockmain.recv(1024).decode()

# # Query the PostgreSQL database 
# pg_cursor.execute(query)
# pg_results = pg_cursor.fetchall()

# # Send the results back to the main machine
# sockmain.sendall(pg_results.encode())