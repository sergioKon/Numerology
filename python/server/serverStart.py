from flask import request, Flask
from pyluach.dates import HebrewDate

from python.appLayer.Gematry import Gematry
from python.appLayer.HebrewGematry import HebGematry
from python.server.response import Response

app = Flask(__name__, static_folder='static', static_url_path='')


@app.route("/")
def hello_world():
    return "<p>bobby.com</p>"


@app.route('/userData')
def userData():
    text_file = open("../web/index.html", "r")
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
'''
    result = 'name = ' + englishName + " birthday =" + birthday + " gematry = " + str(dateCode)
    result = (result + " hebrew name = " + hebrew + " gematry by date = " + str(hebDateCode) +
              " birthday = " + toDate(heb_gematry.date) + " gematry hebrew name =" + str(hebNameCode))
    return result
    '''


def toDate(date: HebrewDate):
    day = str(date.day)
    if len(day) == 1:
        day = '0' + day

    month = str(date.month)
    if len(month) == 1:
        month = '0' + month
    result = day + "/" + month + "/" + str(date.year)
    return result


port_number = 5000

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port_number)

