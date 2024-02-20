from flask import request, Flask
from pyluach.dates import HebrewDate
import sys, os 

sys.path.insert(0, os.getcwd())

from src.appLayer.Gematry import Gematry
from src.appLayer.HebrewGematry import HebGematry
from src.server.response import Response
import traceback 

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/userData', methods=['GET'])
def userData():
    htmlFile= 'userData.html'
    try:
        htmlPath= os.getcwd() + "/src/web/" + htmlFile
        text_file = open(file= htmlPath,mode= "r", encoding='UTF-8')
        data = text_file.read()
        text_file.close()
        return data
    except:
        traceback.print_exc() 
        return "can't read file  " + htmlPath
    # return app.send_static_file('galaxy.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        birthday = request.form.get("birthday")
        englishName = request.form.get("EnglishName")
        gematry = Gematry(birthday, englishName)
        
        englishDateCode = gematry.dateToCode()
        hebrew = request.form.get("HebrewName")

        hebGematry = HebGematry(birthday, hebrew)
        hebDateCode = hebGematry.dateCode
        hebDate= hebGematry.date
        hebNameCode = hebGematry.nameCode

        response = Response(birthday, englishDateCode, hebDate, hebDateCode)
        return  response.toString()
    except:
        traceback.print_exc() 
        return "invalid input"

port_number = 5000

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port_number)
