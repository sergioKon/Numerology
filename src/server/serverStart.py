from flask import request, Flask,  render_template 

from pyluach.dates import HebrewDate
import sys, os 

sys.path.insert(0, os.getcwd())

from src.appLayer.Gematry import Gematry
from src.appLayer.HebrewGematry import HebGematry
from src.server.response import Response
import traceback 

app=Flask(__name__,template_folder='../web/')

@app.route("/index") 
def hello(): 
    return render_template('index.html') 

@app.route('/userData', methods=['GET'])
def userData():
    return render_template('userData.html') 

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
        
        result = Response(birthday, englishDateCode, hebDate, hebDateCode)
        return render_template('result.html') 
    except:
        traceback.print_exc() 
        return "invalid input"
if(len(sys.argv)==1 ):
   port_number = 5000
else: 
    port_number = sys.argv[1]
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port_number)
