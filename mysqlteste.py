import mysql.connector
from mysql.connector import errorcode
try:
	db_connection = mysql.connector.connect(host='172.31.255.2/admin/sql_admin/', user='root', password='vertrigo', database='mkradius')
	print("Database connection made!")
except mysql.connector.Error as error:
	if error.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database doesn't exist")
	elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("User name or password is wrong")
	else:
		print(error)
else:
	db_connection.close()