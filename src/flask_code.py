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
        return None

    mydb.close()

    res = '''
    <table border="1">
        <tr>
            <td>Time</td>
            <td>{}</td>
        </tr>
        <tr>
            <td>Ram Usage</td>
            <td>{}%</td>
        </tr>
    </table>'''.format(str(data[0][1]), str(data[0][2]))



    return res


@app.route('/ram/<time>')
def get_results(time):
    print("here", time)
    try:
        mydb = connect_to_db()
    except mysql.connector.Error as error:
        print("failed to connect", error)
        return error
    res = get_html_results(time)
    return res


if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = '8080')