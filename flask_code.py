import mysql.connector
from util import *


from flask import Flask
app = Flask(__name__)


# Getting ram usage at particular time from local db
def get_html_results(time):
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    query = '''SELECT * FROM ram_values
                           WHERE TIME = (
                           SELECT TIME
                           FROM ram_values
                           ORDER BY ABS(TIMEDIFF(TIME, %s))
                           LIMIT 1
                           );'''

    try:
        mycursor.execute(query, (time,))
        data = mycursor.fetchall()
    except mysql.connector.Error as error:
        print("Data retrieval failed", error)
        mydb.close()
        return error

    mydb.close()

    res = """
       <html>
    <body>
      <p>
        <span style="width: 50px;">Time</span>
        <span style="width: 50px;">Ram Usage</span>
      </p>
      <p>
        <span style="width: 50px;">{}</span>
        <span style="width: 50px;">{}</span>
      </p>
    </body>
    </html>
    """.format(str(data[0][1]), str(data[0][2]))

    return res


@app.route('/ram/<time>')
def get_results(time):
    try:
        mydb = connect_to_db()
    except mysql.connector.Error as error:
        print("failed to connect", error)
        return error
    res = get_html_results(time)
    return res


if __name__ == '__main__':
   app.run()