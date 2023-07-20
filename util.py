from dotenv import dotenv_values
import mysql.connector

config = dotenv_values("credentials.env")
# host = 'host.docker.internal',


def connect_to_db():
    try:
        print(config)
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