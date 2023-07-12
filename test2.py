import psutil
from datetime import datetime
import mysql.connector
import mysql.connector


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='alifaheem',
    port = '3306',
    database = 'ram_storage'
)

mycursor = mydb.cursor()

time= "16:00:12"



# query = '''SELECT * FROM ram_values
#                     WHERE TIME = (
#                     SELECT TIME
#                     FROM ram_values
#                     ORDER BY ABS(TIMEDIFF(TIME, %s))
#                     LIMIT 1
#                     );'''
#
# mycursor.execute(query,(time,))
#
# data = mycursor.fetchall()
#
# for row in data:
#     print(row[0],str(row[1]),row[2])