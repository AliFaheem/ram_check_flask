from dotenv import dotenv_values
import mysql.connector
import psutil
config = dotenv_values("credentials.env")
# host = 'host.docker.internal',


def connect_to_db():
    try:
        mydb = mysql.connector.connect(
            host=config["DB_HOST"],
            user=config["DB_USER"],
            password=config["DB_PASS"],
            port=config["DB_PORT"],
            database=config["DB_NAME"],
        )
    except mysql.connector.Error as error:
        print("failed to connect", error)
        return error
    return mydb

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