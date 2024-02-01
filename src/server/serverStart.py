from flask import request, Flask
from pyluach.dates import HebrewDate
import sys, os 

sys.path.insert(0, os.getcwd())

from src.appLayer.Gematry import Gematry
from src.appLayer.HebrewGematry import HebGematry
from src.server.response import Response


app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/userData')
def userData():

    htmlPath= os.getcwd() + "/src/web/" + 'index.html'
    text_file = open(htmlPath, "r")
    data = text_file.read()
    text_file.close()
    return data
    # return app.send_static_file('galaxy.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        birthday = request.form.get("birthday")
        englishName = request.form.get("EnglishName")
        gematry = Gematry(birthday, englishName)
        gematry.dateToCode()
        dateCode = gematry.dateCode
        hebrew = request.form.get("HebrewName")

        heb_gematry = HebGematry(birthday, hebrew)
        hebDateCode = heb_gematry.dateCode
        hebNameCode = heb_gematry.nameCode

        response = Response(hebNameCode, dateCode,hebDateCode)
        resp  = response.toString()
        return resp
    except:
        return "invalid input"

port_number = 5000

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port_number)
