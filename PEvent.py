class Event:
    _description=""
    _date=None

    def __init__(self):
        self._description=""
        self._date=None

    def getDescription(self):
        return self._description

    def setDescription(self, desc):
        self._description=desc

    def getDate(self):
        return self._date

    def setDate(self, date):
        self._date=date