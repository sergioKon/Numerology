import json


class Response:

    def __init__(self, hebNameCode: int, engDateCode: int, hebrewDateCode: str):
        self.hebrewNameCode = hebNameCode
        self.englishDateCode = engDateCode
        self.aspiration = hebrewDateCode
        self.delta1 = abs(hebrewDateCode - engDateCode)
        self.delta2 = abs(self.aspiration- self.englishDateCode)

    def toString(self):
        response = json.dumps(self, default=lambda o: o.__dict__)
        return response
    