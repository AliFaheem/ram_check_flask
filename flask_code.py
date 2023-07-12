import mysql.connector

from flask import Flask
app = Flask(__name__)


@app.route('/ram/<time>')
def get_results(time):
    try:
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='alifaheem',
            port='3306',
            database='ram_storage'
        )

    except mysql.connector.Error as error:
        print("failed to connect", error)

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
    return str("Time" + '\t\t' + "Ram Usage"+"<br/>" +  str(data[0][1]))+"\t\t\t"+str(data[0][2])

if __name__ == '__main__':
   app.run()