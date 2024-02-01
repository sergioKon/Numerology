class Gematry:
    def __init__(self, date: str, name : str):
        self.dateCode = None
        self.language = 'English'
        self.name= name
        self.date = date
        self.day = date[8:10]
        self.month = date[5:7]
        self.year = date[0:4]

#
    def dateToCode(self):
        result = self.halfWay(self.day)
        result = result + self.halfWay(self.month)
        result = result + self.halfWay(self.year)
        if result > 9:
            result = self.halfWay(result)
        self.dateCode = result

    def halfWay(self, number : int):
        remainder = int(number)
        sum = 0
        while remainder > 0:
            sum = sum + remainder % 10
            remainder = int(remainder / 10)
        if sum > 9:
            sum = self.halfWay(sum)
        return sum



'''
gematry = Gematry("11/01/1970")
gematry.calculate()
gematry.show()

'''
