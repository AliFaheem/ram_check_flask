# This is a sample Python script.
import time
import psutil
from datetime import datetime
import mysql.connector


from util import *

# This function inserts ranm usage values to local db
def insert_values(mydb, current_time, ram_usage):

    # creating query to insert the rmusage values in the db
    mySql_insert_query = "INSERT INTO ram_values (TIME,RAM) VALUES (%s,%s)"
    mycursor = mydb.cursor()  # cursor object to communicate with db


    # creating record to add to local db
    record = (current_time, psutil.virtual_memory()[2])

    try:
        # Inserting values to local db
        mycursor.execute(mySql_insert_query, record)
        mydb.commit()

    except mysql.connector.Error as error:
        print("Data insertion failed", error)
        mydb.close() #closing the connection


def main():
    try:
        mydb = connect_to_db()
    except mysql.connector.Error as error:
        print("failed to connect", error)
        return None


    while True:
        # getting current time
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        # getting current ram usage
        ram_usage = psutil.virtual_memory()[2]

        # inserting values to db
        insert_values(mydb, current_time, ram_usage)

        time.sleep(15)

if __name__ == "__main__":
    main()



