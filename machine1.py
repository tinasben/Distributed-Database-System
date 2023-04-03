import mysql.connector
import socket

# Connect to the MySQL database
mysql_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'school'
}

mysql_conn = mysql.connector.connect(**mysql_config)
mysql_cursor = mysql_conn.cursor()

# Create a socket for connecting to the main machine
sockmain = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockmain.connect(('machine1_ip', 'machine1_port'))

# Receive the query from main machine
query = sockmain.recv(1024).decode()

# Query the MySQL database 
mysql_cursor.execute(query)
mysql_results = mysql_cursor.fetchall()

# Send the results back to the main machine
sockmain.sendall(mysql_results.encode())