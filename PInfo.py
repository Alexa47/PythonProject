import datetime
import random
from PEnergyBalance import *
from PShoppingList import *

class Info:

    def prepareFile(self, filename):
        with open(filename) as filehandle:
            lines=filehandle.readlines()
        with open(filename, 'w') as filehandle:
            lines=filter(lambda x:x.strip(), lines)
            filehandle.writelines(lines)


    def getDate(self):
        today=datetime.datetime.today()
        day=str(today.day)
        month=str(today.month)
        year=str(today.year)
        dateInfo=day+"."+month+"."+year
        return dateInfo

    def nameInfo(self):
        return "Witaj!"

    def readListFromFile(self, filename):
        list=[]
        file=open(filename, 'r', encoding="utf8")
        for line in file:
            list.append(line)
        file.close()
        return list

    def writeListToFile(self, list, filename):
        try:
            f=open(filename, "w")
            for i in range(0, len(list)):
                f.write(list[i]+"\n")
            f.close()
        except FileNotFoundError:
            print("Niepoprawna nazwa pliku")

    def saveEvent(self, event):
        list=[]
        self.prepareFile('terminarz.txt')
        list=self.readListFromFile('terminarz.txt')
        record=str(event.getDate().day)+"."+str(event.getDate().month)+"."+str(event.getDate().year)+"-"+str(event.getDate().hour)+":"+\
               str(event.getDate().minute)+"-"+event.getDescription()
        list.append(record)
        self.writeListToFile(list, 'terminarz.txt')

    def writeToFile(self, balance, list):
        date=""
        today=datetime.datetime.now()
        date+=str(today.day)+"."+str(today.month)+"."+str(today.year)+";"+str(today.hour)+":"+str(today.minute)

        amount=str(balance.getCalAmount())

        list_s=list.getList()

        temp=[]
        temp.append(date)
        temp.append(amount)
        temp.append("LISTA")

        for i in range(0, len(list_s)):
            temp.append(list_s[i])

        self.prepareFile("baza.txt")
        self.writeListToFile(temp, 'baza.txt')

    def readShoppingList(self):
        counter=0
        list=[]
        self.prepareFile('baza.txt')
        fileBase = open('baza.txt', 'r')
        for line in fileBase:
            counter=counter+1
            if(counter>3 and line.rstrip()):
                list.append(line)
        fileBase.close()
        return list

    def saveShoppingList(self, shoppingList):
        counter=0
        list=[]
        self.prepareFile('baza.txt')
        fileBase = open('baza.txt', 'r')
        for line in fileBase:
            counter+=1
            if(counter<4):
                list.append(line)

        for elem in shoppingList.getList():
            list.append(elem)
        self.writeListToFile(list, 'baza.txt')

    def readBalance(self):
        self.prepareFile('baza.txt')
        list=self.readListFromFile('baza.txt')
        balance=float(list[1])
        return balance

    def saveBalance(self, energyBalance):
        list=self.readListFromFile('baza.txt')
        balance=str(energyBalance.getCalAmount())
        list[1]=balance
        self.writeListToFile(list, 'baza.txt')

    def productsList(self):
        self.prepareFile('kalorie.txt')
        temp=self.readListFromFile('kalorie.txt')

        myList=[]
        for i in range(0, len(temp)):
            splitRecord=temp[i].split()
            name=""
            for j in range(0, len(splitRecord)-1):
                name+=splitRecord[j]+" "
            myList.append(name)
        return myList

    def sportsList(self):
        self.prepareFile('sport.txt')
        temp=self.readListFromFile('sport.txt')

        myList = []
        for i in range(0, len(temp)):
            splitRecord = temp[i].split()
            name = ""
            for j in range(0, len(splitRecord) - 1):
                name += splitRecord[j] + " "
            myList.append(name)
        return myList

    def getSavedDate(self):
        self.prepareFile('baza.txt')
        list=self.readListFromFile('baza.txt')
        temp=list[0].split(";")
        return temp[0]

    def checkDate(self, date):
        currentDate=self.getDate()
        if(currentDate==date):
            return True
        else:
            return False

    def prepareDatabase(self):
        eb=EnergyBalance()
        sl=ShoppingList()
        sl.setList(self.readShoppingList())
        savedDate=self.getSavedDate()
        if(self.checkDate(savedDate)==False):
            eb.clear()
            self.writeToFile(eb, sl)

    def getTodaysPlan(self, template):
        self.prepareFile('terminarz.txt')
        list=self.readListFromFile('terminarz.txt')

        temp=[]
        sortingTemplate=[]
        offset=len(template)
        for i in range(0, len(list)):
            record=list[i]
            if(record[0:offset]==template):
                temp.append(record)

        newList=[]
        for j in range(0, len(temp)):
            current=temp[j]
            hour=current[offset+1: current.index(":")]
            newRecord=current[offset+1: len(current)-1]
            sortingTemplate.append(int(hour))
            newList.append(newRecord)

        sortedList=[x for y ,x in sorted(zip(sortingTemplate, newList))]
        str_list=""
        for z in range(0, len(sortedList)):
            str_list+=sortedList[z]+"\n"
        return str_list

    def saveBurnt(self, amount):
        self.prepareFile('spalono.txt')
        list=self.readListFromFile('spalono.txt')

        current=float(list[len(list)-1])
        print("current", current)
        current+=amount
        list.pop(len(list)-1)
        list.append(str(current))
        self.writeListToFile(list, 'spalono.txt')

    def getBurnt(self):
        self.prepareFile('spalono.txt')
        list=self.readListFromFile('spalono.txt')
        burnt=list[len(list)-1]
        balance = float("{:.2f}".format(float(burnt)))
        return balance

    def saveEaten(self, amount):
        self.prepareFile("przyjeto.txt")
        list=self.readListFromFile('przyjeto.txt')
        current = float(list[len(list) - 1])
        current += amount
        list.pop(len(list) - 1)
        list.append(str(current))
        self.writeListToFile(list, 'przyjeto.txt')

    def getEaten(self):
        self.prepareFile("przyjeto.txt")
        list=self.readListFromFile('przyjeto.txt')
        return list[len(list) - 1]

    def chooseQuote(self):
        list = self.readListFromFile('cytat.txt')
        offset=random.randint(0, len(list)-1)
        return list[offset]

    def prepareTemps(self, filename):
        list=self.readListFromFile(filename)
        savedDate=list[0].rstrip()

        if(self.checkDate(savedDate)==False):
            print("czyszczę", filename)
            now = datetime.datetime.now()
            try:
                f = open(filename, "w")
                f.write(str(now.day)+"."+str(now.month)+"."+str(now.year)+"\n")
                f.write("0.0")
                f.close()
            except:
                print("Niepoprawna nazwa pliku")





