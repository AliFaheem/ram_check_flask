# This is a sample Python script.
import time
import psutil
from datetime import datetime
import mysql.connector
from dotenv import dotenv_values

config = dotenv_values("credentials.env")


# Connecting to local db
def connect_to_db():
    try:
        mydb = mysql.connector.connect(
            host=config["DB_HOST"],
            user=config["DB_USER"],
            password=config["DB_PASS"],
            port = config["DB_PORT"],
            database = config["DB_NAME"]
        )
    except mysql.connector.Error as error:
        print("failed to connect",error)
        return None
    return mydb

# This function inserts ran usage values to local db
def inser_values(mydb, current_time, ram_usage):

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
    mydb = connect_to_db()
    while True:
        # getting current time
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        # getting current ram usage
        ram_usage = psutil.virtual_memory()[2]

        # inserting values to db
        inser_values(mydb, current_time, ram_usage)

        time.sleep(15)

if __name__ == "__main__":
    main()


