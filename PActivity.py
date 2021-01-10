class Activity:
    _activities=[]

    def __init__(self):
        self._activities=[]

    def getActvities(self):
        return self._activities

    def setActivities(self, activityList):
        self._activities=activityList

    def addActivity(self, activity):
        self._activities.append(activity)

    def getAmount(self, activity):
        temp=activity.split()
        amount=float(temp[len(temp)-1])
        return amount

    def findActivityCountCalories(self, activity):
        fileActivities=[]
        fileSport=open('sport.txt', 'r', encoding="utf8")
        for line in fileSport:
            fileActivities.append(line)

        counter=0.0

        for i in range(0, len(fileActivities)):
            record=fileActivities[i]
            currentName=""
            tempName=record.split()

            for z in range(0, len(tempName)-1):
                currentName+=tempName[z]+" "
                
            temp=activity.split()
            name=""
            for j in range(0, len(temp)-1):
                name+=temp[j]+" "

            if(currentName==name):
                calories=self.getAmount(record)
                amount=self.getAmount(activity)
                counter=calories*amount*0.016
        fileSport.close()
        return -counter

    def countCalories(self):
        totalCounter=0.0
        for i in range(0, len(self._activities)):
            record=self._activities[i]
            totalCounter+=self.findActivityCountCalories(record)
        return totalCounter

