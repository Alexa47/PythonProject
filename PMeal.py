class Meal:

    _title=""
    _ingredients=[]

    def __init__(self):
        self._title=""
        self._ingredients=[]

    def getTitle(self):
        return self._title

    def setTitle(self, text):
        self._title=text

    def getIngredients(self):
        return self._ingredients

    def setIngredients(self, list):
        self._ingredients=list

    def addIngredient(self, ingredient):
        self._ingredients.append(ingredient)

    def getAmount(self, ingredient):
        temp=ingredient.split()
        amount=float(temp[len(temp)-1])
        return amount

    def findProductGetCalories(self, product):
        balance=0.0
        fileProducts=[]
        fileBase = open('kalorie.txt', 'r', encoding="utf8")
        for line in fileBase:
            fileProducts.append(line)

        temp=product.split()
        name=""
        for i in range(0, len(temp)-1):
            name+=temp[i]+" "
        offset=len(name)

        for j in range(0, len(fileProducts)):
            record=fileProducts[j]
            if(record.__contains__(name) and record[0:offset]==name):
                calories=self.getAmount(record)
                amount=self.getAmount(product)
                balance=calories*amount*0.01
        fileBase.close()
        return balance

    def countCalories(self):
        counter=0.0
        for i in range(0, len(self._ingredients)):
            record=self._ingredients[i]
            counter+=self.findProductGetCalories(record)
        return counter


