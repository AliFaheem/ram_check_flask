# This is a sample Python script.
import time
import psutil
from datetime import datetime
import util



def main():

    while True:
        # getting current time
        mydb = util.connect_to_db()

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        # getting current ram usage
        ram_usage = psutil.virtual_memory()[2]

        # inserting values to db
        util.insert_values(mydb, current_time, ram_usage)

        time.sleep(15)

if __name__ == "__main__":
    main()



