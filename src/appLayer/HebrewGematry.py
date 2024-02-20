from pyluach import dates as HebrewDate, hebrewcal

from src.appLayer.Gematry import Gematry as Base

class HebGematry(Base):
    letters = {'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
               'י': 10, 'ך': 20, 'כ': 20, 'ל': 30, 'ם': 40, 'מ': 40, 'ן': 50, 'ן': 50,
               'ס': 60, 'ע': 70, 'פ': 80, 'ף': 80, 'ץ': 90, 'צ': 90, 'ק': 100, 'ר': 200,
               'ש': 300, 'ת': 400}

    def __init__(self, date: str, name):
        self.nameCode = None
        self.name = name
        super().__init__(date,name)
        gredDate = HebrewDate.GregorianDate(int(self.year), int(self.day), int(self.month))
        self.date = gredDate.to_heb()

        self.day = self.date.day
        self.month = self.date.month
        self.year = self.date.year
        self.dateToCode()
        self.convertName()

    def convertName(self):
        firstName = self.name.split()[0]
        lastName = self.name.split()[1]

        total = self.__worldToInt(firstName)
        total = total + self.__worldToInt(lastName)
        self.nameCode = self.halfWay(total)

    def __worldToInt(self, world):
        total = 0
        for symbol in world:
            digit = self.letters.get(symbol)
            digit = str(digit)[0:1]
            total = total + int(digit)
        return total

    def show(self):
        print(" gematry by date  = ", self.dateCode)
        print(" gematry by name  = ", self.nameCode)
   
    @staticmethod
    def dateToText(date : HebrewDate):
        hebrewcal.hebrew_date_string(True)
'''
hebGematry = HebGematry("11/01/1970", "בוריס פיין ")
hebGematry.convertName()
hebGematry.show()
'''