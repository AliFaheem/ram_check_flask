# This is a sample Python script.
import time

import psutil
from datetime import datetime
import mysql.connector


try:
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='alifaheem',
        port = '3306',
        database = 'ram_storage'
    )

except mysql.connector.Error as error:
    print("failed to connect",error)


mySql_insert_query = "INSERT INTO ram_values (TIME,RAM) VALUES (%s,%s)"
mycursor = mydb.cursor()

while(True):

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    record = (current_time,psutil.virtual_memory()[2])
    try:
        mycursor.execute(mySql_insert_query, record)
        mydb.commit()
    except mysql.connector.Error as error:
        print("Data insertion failed", error)
        mydb.close()

    time.sleep(15)

