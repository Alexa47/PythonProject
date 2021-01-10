class EnergyBalance:
    _calAmount=0

    def __init__(self):
        self._calAmount=0

    def getCalAmount(self):
        return self._calAmount

    def setCalAmount(self, amount):
        self._calAmount+=amount

    def clear(self):
        self._calAmount=0
        print("cleared")
