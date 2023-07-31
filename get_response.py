from util import connect_to_db
import datetime
import json

def seconds_to_time_format(seconds):
    time_format = str(datetime.timedelta(seconds=seconds))
    return time_format


def validate_input(time):
    if (len(time.split(":"))) <= 3:
        return True
    else:
        return False


def get_html_results(time):
    mydb = connect_to_db()
    mycursor = mydb.cursor()

    if not validate_input(time):
        return []

    if len(time.split(":")) == 1:
        query = """SELECT *
            FROM ram_values
            WHERE HOUR(TIME) = %s;"""

    if len(time.split(":")) == 2:
        query = """SELECT *
               FROM ram_values
               WHERE HOUR(TIME) = %s
               AND MINUTE(TIME) = %s;"""

    if len(time.split(":")) == 3:
        query = """SELECT *
               FROM ram_values
               WHERE HOUR(TIME) = %s
               AND MINUTE(TIME) = %s
               AND SECOND(TIME) = %s;"""

    try:
        mycursor.execute(query, (time.split(":")))
        data = mycursor.fetchall()
    except mysql.connector.Error as error:
        print("Data retrieval failed", error)
        mydb.close()
        return None

    mydb.close()

    converted_data = [
        {"time": str(datetime.timedelta(seconds=item[1].seconds)), "value": item[2]}
        for item in data
    ]

    j_data = json.dumps(converted_data, indent=3)

    return j_data
