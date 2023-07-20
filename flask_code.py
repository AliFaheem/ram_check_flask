from get_response import *

from flask import Flask
app = Flask(__name__)


@app.route('/ram/<time>')
def get_results(time):
    res = get_html_results(time)
    return res


if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = '8080')