from dotenv import dotenv_values
import mysql.connector

config = dotenv_values("credentials.env")

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