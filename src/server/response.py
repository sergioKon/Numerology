import json
from pyluach import dates as HebrewDate, hebrewcal

class Response:

    def __init__(self,engDate : str, engDateCode : int , hebDate : HebrewDate, hebDateCode : int ):
         self.engDate= engDate
         self.engDateCode=engDateCode
         self.hebDate=hebDate
         
         hebDay= self.__digitToString(hebDate.day)
         hebMonth= self.__digitToString(hebDate.month)
         hebYear= hebDate.year
        
         self.hebrewFormat= str(hebDay) + "/" + str(hebMonth) +"/" + str(hebYear)
         self.hebDateCode=hebDateCode
 
    # private method
    def  __digitToString(self, value : int):
        if value < 9:
            return  '0'+ str(value) 
        return  str(value)
    
    def toString(self):

        day = self.engDate[8:10]
        month = self.engDate[5:7]
        year =self.engDate[0:4]
        engDate = day+"/"+ month+"/"+ year

        output=' תאריך לועזי  ' + engDate + ' - ' + ' תוצאה ' + str(self.engDateCode) 
        output= output + "<br>"

        output = output + ' תאריך עברי ' + self.hebrewFormat + '  תוצאה = ' + str(self.hebDateCode) 
        output= output + "<br>"

        delta= abs(self.hebDateCode - self.engDateCode)
        output= output + ' הפרש ' + str(delta) + "<br>"
        #response = json.dumps(self, default=lambda o: o.__dict__)
        return output
    