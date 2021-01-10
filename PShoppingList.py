class ShoppingList:
    _list=[]

    def __init__(self):
        self._list=[]

    def getList(self):
        return self._list

    def setList(self, list):
        self._list=list

    def addProduct(self, product):
        self._list.append(product)

    def removeProduct(self, product):
        self._list.remove(product)

    def getElem(self, offset):
        return self._list[offset]

    def clearList(self):
        self._list.clear()

    def display(self):
        list_main=""
        for i in range(0, len(self._list)):
            list_main+=self._list[i]
        return list_main