import tkinter
from tkinter import ttk, SUNKEN
from tkcalendar import *


from PActivity import *
from PInfo import *
from PEvent import *
from PMeal import *

inf=Info()
inf.prepareDatabase()
inf.prepareTemps("spalono.txt")
inf.prepareTemps("przyjeto.txt")

food=inf.productsList()
sports=inf.sportsList()
gender=["kobieta", "mężczyzna"]
act=["brak aktywności", "niska aktywność", "średnia aktywność- praca siedząca + 1/2 treningi tyg", "wysoka aktywność- częste treningi bądź praca fizyczna", "zawodowi sportowcy"]


class MainWindow():
    def __init__(self, master):
        self.master=master

        self.labelNameInfo=tkinter.Message(master, text=inf.nameInfo()+"\n"+inf.getDate()+"\n"+inf.chooseQuote(), bg="wheat1", fg="navy", font=("Helvetica", 16), borderwidth=5, relief=tkinter.RIDGE)
        self.labelNameInfo.grid(row=1, column=1, pady=(10,10))

        today = datetime.datetime.now()
        template = str(today.day) + "." + str(today.month) + "." + str(today.year)

        self.labelMsg=tkinter.Message(master, text="PLAN DNIA", bg="wheat1", fg="navy",  font=("Helvetica", 24), relief=tkinter.RIDGE, borderwidth=5).grid(row=1, column=2, padx=100)
        self.labelPlan=tkinter.Message(master, text=inf.getTodaysPlan(template), fg="navy", borderwidth=25, relief=tkinter.RIDGE, font=("Helvetica", 12)).grid(row=2, column=2, pady=(0, 0), padx=0)

        self.frameButtons=tkinter.Frame(master, width=100, height=300)
        self.frameButtons.grid(row=2, column=1)

        self.btnAddEvent=tkinter.Button(self.frameButtons, text="Dodaj wydarzenie", command=self.addEventWindow, bg="plum2", fg="navy", font=("Helvetica", 11), width=16, borderwidth=5, relief=tkinter.RIDGE).grid(row=1, column=1)
        self.btnShoppingList=tkinter.Button(self.frameButtons, text="Lista zakupów", command=self.shoppingListWindow, bg="plum2", fg="navy", font=("Helvetica", 11), width=16, borderwidth=5, relief=tkinter.RIDGE).grid(row=2, column=1)
        self.btnBalance=tkinter.Button(self.frameButtons, text="Bilans kaloryczny", command=self.balanceDispleyWindow, bg="plum2", fg="navy", font=("Helvetica", 11), width=16, borderwidth=5, relief=tkinter.RIDGE).grid(row=3, column=1)
        self.btnDate=tkinter.Button(self.frameButtons, text="Przejdź do daty", command=self.chooseDateWindow, bg="plum2", fg="navy", font=("Helvetica", 11), width=16, borderwidth=5, relief=tkinter.RIDGE).grid(row=5, column=1)
        self.btnExit=tkinter.Button(self.frameButtons, text="Wyjdź", command=self.quit, bg="plum2", fg="navy", font=("Helvetica", 11), width=16, borderwidth=5, relief=tkinter.RIDGE).grid(row=6, column=1)
        self.btnCount=tkinter.Button(self.frameButtons, text="Wydatek energetyczny", command=self.countBalanceWindow, bg="plum2", fg="navy", font=("Helvetica", 11), width=16, borderwidth=5, relief=tkinter.RIDGE).grid(row=4, column=1)

    def addEventWindow(self):
        self.master.withdraw()
        toplevel = tkinter.Toplevel(self.master)
        toplevel.geometry("500x400")
        toplevel.config(bg="DarkSeaGreen1")
        app = AddEventWindow(toplevel)

    def shoppingListWindow(self):
        self.master.withdraw()
        toplevel = tkinter.Toplevel(self.master)
        toplevel.geometry("400x300")
        toplevel.config(bg="honeydew2")
        toplevel.resizable(height = None, width = None)
        app = ShoppingListWindow(toplevel)

    def balanceDispleyWindow(self):
        self.master.withdraw()
        toplevel = tkinter.Toplevel(self.master)
        toplevel.geometry("400x300")
        toplevel.config(bg="azure")
        app = BalanceDisplayWindow(toplevel)

    def chooseDateWindow(self):
        self.master.withdraw()
        toplevel = tkinter.Toplevel(self.master)
        toplevel.geometry("500x600")
        toplevel.config(bg="LavenderBlush2")
        app = ChooseDateWindow(toplevel)

    def quit(self):
        self.master.quit()

    def countBalanceWindow(self):
        self.master.withdraw()
        toplevel=tkinter.Toplevel(self.master)
        toplevel.geometry("800x400")
        toplevel.config(bg="LemonChiffon2")
        app=BalanceCountWindow(toplevel)

class AddEventWindow:
    def __init__(self, master):
        self.master = master

        self.labelTime=tkinter.Label(master, text="Godzina", fg="ForestGreen", bg="DarkSeaGreen1", font=("Helvetica", 12),
                                     borderwidth=5, relief=tkinter.RIDGE).grid(row=1, column=1, pady=10)
        self.cal=Calendar(master, selectmode="day", year=2021, month=1, day=2)
        self.cal.grid(row=2, column=2, pady=10)
        self.labelDate=tkinter.Label(master, text="Data", fg="ForestGreen", bg="DarkSeaGreen1", font=("Helvetica", 12),
                                     borderwidth=5, relief=tkinter.RIDGE).grid(row=2, column=1, pady=10)
        self.labelDesc=tkinter.Label(master, text="Opis", fg="ForestGreen", bg="DarkSeaGreen1", font=("Helvetica", 12),
                                     borderwidth=5, relief=tkinter.RIDGE).grid(row=3, column=1, pady=10)

        self.e1=tkinter.Entry(master)
        self.e1.grid(row=1, column=2, pady=10)
        self.e3=tkinter.Entry(master)
        self.e3.grid(row=3, column=2, pady=10)

        self.btnAdd=tkinter.Button(master, text="OK", command=lambda:[self.getDate(self.e1.get(), self.e3.get()), self.back()],
                fg="ForestGreen", bg="DarkSeaGreen3", font=("Helvetica", 11), borderwidth=5, relief=tkinter.RIDGE).grid(row=4, column=2, padx=250)
        self.btnExit=tkinter.Button(master, text="Wyjdź",  fg="ForestGreen", bg="DarkSeaGreen3", font=("Helvetica", 11),
                                    command=self.back, borderwidth=5, relief=tkinter.RIDGE).grid(row=4, column=1)

    def back(self):
        self.master.withdraw()
        toplevel = tkinter.Toplevel(self.master)
        toplevel.config(bg="wheat1")
        toplevel.resizable(True, True)
        app = MainWindow(toplevel)

    def getDate(self, time, desc):
        date=str(self.cal.get_date())
        temp=date.split("/")
        act_date=temp[1]+"-"+temp[0]+"-20"+temp[2]
        self.addEvent(time, act_date, desc)

    def addEvent(self, time, date, description):
        temp_date = date.split("-")
        try:
            temp_time = time.split(":")
            date = datetime.datetime(int(temp_date[2]), int(temp_date[1]), int(temp_date[0]), int(temp_time[0]),int(temp_time[1]))
            ev = Event()
            ev.setDate(date)
            ev.setDescription(description)
            inf.saveEvent(ev)
        except:
            print("Błędny format godziny")

class ShoppingListWindow():
    def __init__(self, master):
        self.master=master

        self.sl=ShoppingList()
        self.sl.setList(inf.readShoppingList())

        self.labelMain=tkinter.Label(master, text="Lista zakupów", bg="honeydew2", fg="cyan4",
                    font=("Helvetica", 16), borderwidth=5, relief=tkinter.RIDGE).grid(row=1, column=1, pady=10, padx=50)
        self.labelList=tkinter.Label(master, text=self.sl.display(), fg="cyan4",
                                     font=("Helvetica", 12), bg="gray92", borderwidth=5, relief=tkinter.RIDGE)
        self.labelList.grid(row=2, column=1, padx=50, pady=10)

        self.btnAddToList=tkinter.Button(master, text="Dodaj", command=self.addWindow, bg="gray92", fg="cyan4",
                                         font=("Helvetica", 11), borderwidth=5, relief=tkinter.RIDGE).grid(row=3, column=1)
        self.btnBack=tkinter.Button(master, text="Wyjdź", command=self.back, bg="gray92", fg="cyan4",
                                    font=("Helvetica", 11), borderwidth=5, relief=tkinter.RIDGE ).grid(row=3, column=2)
        self.btnClear=tkinter.Button(master, text="Wyczyść", command=self.clearShoppingList, bg="gray92", fg="cyan4",
                                     font=("Helvetica", 11), borderwidth=5, relief=tkinter.RIDGE ).grid(row=3, column=3)

    def addWindow(self):
        self.master.withdraw()
        toplevel = tkinter.Toplevel(self.master)
        toplevel.geometry("400x200")
        toplevel.config(bg="honeydew2")
        app = ShoppingListAddWindow(toplevel)

    def back(self):
        self.master.withdraw()
        toplevel = tkinter.Toplevel(self.master)
        toplevel.config(bg="wheat1")
        toplevel.resizable(True, True)
        app = MainWindow(toplevel)

    def clearShoppingList(self):
        sl = ShoppingList()
        sl.clearList()
        inf.saveShoppingList(sl)
        self.labelList.config(text="")


class ShoppingListAddWindow():
    def __init__(self, master):
        self.master=master

        self.labelInfo=tkinter.Label(master, text="Dodawanie produktu do listy zakupów",  bg="honeydew2", fg="cyan4", font=("Helvetica", 16), borderwidth=5, relief=tkinter.RIDGE).grid(row=1, column=1)

        self.e1=tkinter.Entry(master)
        self.e1.grid(row=2, column=1, pady=20)

        self.btnOk=tkinter.Button(master, text="Dodaj", command=lambda:[self.addToShoppingList(self.e1.get()), self.back()], bg="gray92", fg="cyan4", font=("Helvetica", 11), borderwidth=5, relief=tkinter.RIDGE).grid(row=3, column=1)
        self.btnBack=tkinter.Button(master, text="Wyjdź", command=self.back, bg="gray92", fg="cyan4", font=("Helvetica", 11), borderwidth=5, relief=tkinter.RIDGE).grid(row=4, column=1)

    def addToShoppingList(self, product):
        sl = ShoppingList()
        sl.setList(inf.readShoppingList())
        sl.addProduct(product)
        inf.saveShoppingList(sl)

    def back(self):
        self.master.withdraw()
        toplevel = tkinter.Toplevel(self.master)
        toplevel.geometry("400x300")
        toplevel.config(bg="honeydew2")
        toplevel.resizable(height=None, width=None)
        app = ShoppingListWindow(toplevel)

class BalanceDisplayWindow():
    def __init__(self, master):
        self.master=master

        self.labelBalance=tkinter.Label(master, text="Bilans na dziś", bg="azure", fg="purple4", font=("Helvetica", 16), borderwidth=5, relief=tkinter.RIDGE).grid(row=1, column=2, pady=10)
        self.labelEaten=tkinter.Label(master, text="Przyjęto", bg="azure", fg="purple4", font=("Helvetica", 12), borderwidth=5, relief=tkinter.RIDGE, width=8).grid(row=2, column=1)
        self.labelBurnt=tkinter.Label(master, text="Spalono", bg="azure", fg="purple4", font=("Helvetica", 12), borderwidth=5, relief=tkinter.RIDGE, width=8).grid(row=3, column=1)
        self.labelTotal=tkinter.Label(master, text="Łącznie", bg="azure", fg="purple4", font=("Helvetica", 12), borderwidth=5, relief=tkinter.RIDGE, width=8).grid(row=4, column=1)

        self.labelAmountE=tkinter.Label(master, text=inf.getEaten(), bg="azure", fg="purple4", font=("Helvetica", 12), borderwidth=5, relief=tkinter.RIDGE, width=8).grid(row=2, column=2)
        self.labelAmountB=tkinter.Label(master, text=inf.getBurnt(), bg="azure", fg="purple4", font=("Helvetica", 12), borderwidth=5, relief=tkinter.RIDGE, width=8).grid(row=3, column=2)

        eb = EnergyBalance()
        if (inf.checkDate(inf.getDate()) == False):
            eb.setCalAmount(0)
            inf.saveBalance(eb)
        else:
            eb.setCalAmount(inf.readBalance())

        sum = float("{:.2f}".format(float(inf.getEaten()) + float(inf.getBurnt())))

        self.labelAmountT=tkinter.Label(master, text=str(sum), bg="azure", fg="purple4", font=("Helvetica", 12), borderwidth=5, relief=tkinter.RIDGE, width=8).grid(row=4, column=2, pady=10)

        self.btnAddMeal=tkinter.Button(master, text="Dodaj posiłek", command=self.productDisplayWindow, bg="azure2", fg="purple4", font=("Helvetica", 11), width=12 ,borderwidth=5, relief=tkinter.RIDGE).grid(row=5, column=1)
        self.btnAddActivity=tkinter.Button(master, text="Dodaj aktywność", command=self.activityDisplayWindow, bg="azure2", fg="purple4", font=("Helvetica", 11), width=12, borderwidth=5, relief=tkinter.RIDGE).grid(row=5, column=2)
        self.btnExit=tkinter.Button(master, text="Wyjdź", command=self.back, bg="azure2", fg="purple4", font=("Helvetica", 11), borderwidth=5, relief=tkinter.RIDGE, width=12).grid(row=5, column=3)

    def productDisplayWindow(self):
        self.master.withdraw()
        toplevel = tkinter.Toplevel(self.master)
        toplevel.geometry("400x300")
        toplevel.config(bg="azure")
        app = ProductsDisplayWindow(toplevel)

    def activityDisplayWindow(self):
        self.master.withdraw()
        toplevel=tkinter.Toplevel(self.master)
        toplevel.geometry("400x300")
        toplevel.config(bg="azure")
        app=ActivityDisplayWindow(toplevel)

    def back(self):
        self.master.withdraw()
        toplevel = tkinter.Toplevel(self.master)
        toplevel.config(bg="wheat1")
        toplevel.resizable(True, True)
        app = MainWindow(toplevel)

class ProductsDisplayWindow():
    def __init__(self, master):
        self.master=master

        self.labelProduct=tkinter.Label(master, text="Produkt", bg="azure", fg="purple4", font=("Helvetica", 16), borderwidth=5, relief=tkinter.RIDGE, width=10).grid(row=1, column=1, pady=10)

        self.variable1 = tkinter.StringVar(master)
        self.variable1.set(food[0])
        self.pp = tkinter.OptionMenu(master, self.variable1, *food)
        self.pp.grid(row=2, column=1)
        self.pp.config(bg="azure", fg="purple4", font=("Helvetica", 12))

        self.labelGrams=tkinter.Label(master, text="Ilość w gramach",bg="azure", fg="purple4", font=("Helvetica", 16)).grid(row=3, column=1, pady=10)
        self.e1 = tkinter.Entry(master)
        self.e1.grid(row=3, column=2)

        self.buttonOk=tkinter.Button(master, text="OK", command=lambda:[self.addToBalance(str(self.variable1.get()), self.e1.get()), self.back()], borderwidth=5, relief=tkinter.RIDGE, bg="azure2", fg="purple4", font=("Helvetica", 11), width=7).grid(row=4, column=1)
        self.buttonManual=tkinter.Button(master, text="Ręcznie", command=self.manualSetWindow, bg="azure2", fg="purple4", font=("Helvetica", 11), borderwidth=5, relief=tkinter.RIDGE, width=7).grid(row=4, column=2)
        self.buttonBack=tkinter.Button(master, text="Wyjdź", command=self.back, bg="azure2", fg="purple4", font=("Helvetica", 11), borderwidth=5, relief=tkinter.RIDGE, width=7).grid(row=4, column=3)

    def addToBalance(self, product, grams):
        record = product + grams
        try:
            ml = Meal()
            ml.addIngredient(record)
            calories = ml.countCalories()
            eb = EnergyBalance()
            total = inf.readBalance() + calories
            eb.setCalAmount(total)
            inf.saveBalance(eb)
            inf.saveEaten(calories)
        except:
            print("Błędne dane")

    def back(self):
        self.master.withdraw()
        toplevel = tkinter.Toplevel(self.master)
        toplevel.geometry("400x300")
        toplevel.config(bg="azure")
        app = BalanceDisplayWindow(toplevel)

    def manualSetWindow(self):
        self.master.withdraw()
        toplevel = tkinter.Toplevel(self.master)
        toplevel.geometry("400x300")
        toplevel.config(bg="azure")
        app = ManualSetWindow(toplevel)

class ManualSetWindow():
    def __init__(self, master):
        self.master=master

        self.labelAmount=tkinter.Label(master, text="Podaj ilość", bg="azure", fg="purple4",font=("Helvetica", 16), borderwidth=5, relief=tkinter.RIDGE).grid(row=1, column=1, pady=10)

        self.e1 = tkinter.Entry(master)
        self.e1.grid(row=2, column=1)
        self.labelKcal=tkinter.Label(master, text="kcal", bg="azure", fg="purple4",
                                     font=("Helvetica", 12)).grid(row=2, column=2, pady=10)

        self.btnOk=tkinter.Button(master, text="OK", command=lambda:[self.addCalories(float(self.e1.get())), self.back()], bg="azure", fg="purple4", font=("Helvetica", 11), width=5,borderwidth=5, relief=tkinter.RIDGE).grid(row=3, column=1)
        self.btnExit=tkinter.Button(master, text="Wyjdź", command=self.back, bg="azure", fg="purple4", font=("Helvetica", 11), borderwidth=5, relief=tkinter.RIDGE, width=5).grid(row=3, column=2)

    def addCalories(self, amount):
        try:
            e = EnergyBalance()
            e.setCalAmount(amount)
            inf.saveBalance(e)
            inf.saveEaten(amount)
        except:
            print("Błędne dane")

    def back(self):
        self.master.withdraw()
        toplevel = tkinter.Toplevel(self.master)
        toplevel.geometry("400x300")
        toplevel.config(bg="azure")
        app = BalanceDisplayWindow(toplevel)

class ActivityDisplayWindow():
    def __init__(self, master):
        self.master=master

        self.labelType=tkinter.Label(master, text="Rodzaj sportu", bg="azure", fg="purple4", font=("Helvetica", 16), borderwidth=5, relief=tkinter.RIDGE ).grid(row=1, column=1, pady=10)
        self.variable1 = tkinter.StringVar(master)
        self.variable1.set(sports[0])
        self.pp = tkinter.OptionMenu(master, self.variable1, *sports)
        self.pp.grid(row=2, column=1)
        self.pp.config(bg="azure", fg="purple4", font=("Helvetica", 12), borderwidth=5, relief=tkinter.RIDGE)

        self.labelMin=tkinter.Label(master, text="Czas trwania w minutach", bg="azure", fg="purple4", font=("Helvetica", 12)).grid(row=3, column=1, pady=10)
        self.e1 = tkinter.Entry(master)
        self.e1.grid(row=3, column=2)

        self.btnOk=tkinter.Button(master, text="OK", command=lambda:[self.addActivity(str(self.variable1.get()), self.e1.get()), self.back()], bg="azure", fg="purple4", font=("Helvetica", 11), borderwidth=5, relief=tkinter.RIDGE, width=7).grid(row=4, column=1)
        self.btnExit=tkinter.Button(master, text="Wyjdź", command=self.back, bg="azure", fg="purple4", font=("Helvetica", 11), borderwidth=5, relief=tkinter.RIDGE, width=7).grid(row=4, column=2)

    def addActivity(self, activity, time):
        try:
            act = activity + time
            at = Activity()
            at.addActivity(act)
            calories = at.countCalories()
            eb = EnergyBalance()
            eb.setCalAmount(inf.readBalance() + calories)
            inf.saveBalance(eb)
            print("saved balance")
            inf.saveBurnt(calories)
        except:
            print("Błędne dane")

    def back(self):
        self.master.withdraw()
        toplevel = tkinter.Toplevel(self.master)
        toplevel.geometry("400x300")
        toplevel.config(bg="azure")
        app = BalanceDisplayWindow(toplevel)

class ChooseDateWindow():
    def __init__(self, master):
        self.master=master

        self.labelDate=tkinter.Label(master, text="Podaj datę", bg="LavenderBlush2", fg="IndianRed4", font=("Helvetica", 16), borderwidth=5, relief=tkinter.RIDGE).grid(row=1, column=1, padx=30)
        self.cal = Calendar(master, selectmode="day", year=2021, month=1, day=2)
        self.cal.grid(row=1, column=2, pady=10)

        self.buttonOk = tkinter.Button(master, text="OK", command=lambda: self.getPlan(self.cal.get_date()), bg="LavenderBlush2", fg="IndianRed4", font=("Helvetica", 11), borderwidth=5, relief=tkinter.RIDGE, width=5).grid(row=2, column=1, pady=10)
        self.btnExit=tkinter.Button(master, text="Wyjdź", command=self.back, bg="LavenderBlush2", fg="IndianRed4", font=("Helvetica", 11), borderwidth=5, relief=tkinter.RIDGE, width=5).grid(row=2, column=2, pady=10)
        self.sep = ttk.Separator(master, orient="horizontal")
        self.sep.grid(row=3, columnspan=100, ipadx=100)

        self.days_plan = tkinter.Label(master, bg="LavenderBlush2", fg="IndianRed4", font=("Helvetica", 12), borderwidth=5, relief=tkinter.RIDGE)
        self.days_plan.grid(row=4, column=1)

    def getPlan(self, date):
        date = str(self.cal.get_date())
        temp = date.split("/")
        act_date = temp[1] + "-" + temp[0] + "-20" + temp[2]
        act_date_tab=act_date.split("-")
        chosenDate=act_date_tab[0]+"."+act_date_tab[1]+"."+act_date_tab[2]
        plan=inf.getTodaysPlan(chosenDate)
        self.days_plan.config(text=plan)

    def back(self):
        self.master.withdraw()
        toplevel = tkinter.Toplevel(self.master)
        toplevel.config(bg="wheat1")
        toplevel.resizable(width=None, height=None)
        app = MainWindow(toplevel)

class BalanceCountWindow():
    def __init__(self, master):
        self.master=master

        self.labelGender=tkinter.Label(master, text="Płeć", font=("Helvetica", 14), bg="LemonChiffon2",
                                borderwidth=5, relief=tkinter.RIDGE, width=15).grid(row=1, column=1)
        self.variable1 = tkinter.StringVar(master)
        self.variable1.set(gender[0])
        self.opp=tkinter.OptionMenu(master, self.variable1, *gender )
        self.opp.config(bg="LemonChiffon2")
        self.opp.grid(row=1, column=2)

        self.labelMass=tkinter.Label(master, text="Waga w kg", font=("Helvetica", 14),
                                bg="LemonChiffon2", borderwidth=5, relief=tkinter.RIDGE, width=15).grid(row=2, column=1)
        self.e1=tkinter.Entry(master)
        self.e1.grid(row=2, column=2)

        self.labelHeight=tkinter.Label(master, text="Wzrost w cm", font=("Helvetica", 14),
                                bg="LemonChiffon2", borderwidth=5, relief=tkinter.RIDGE, width=15).grid(row=3, column=1)
        self.e2=tkinter.Entry(master)
        self.e2.grid(row=3, column=2)

        self.labelAge=tkinter.Label(master, text="Wiek", font=("Helvetica", 14), bg="LemonChiffon2",
                                    borderwidth=5, relief=tkinter.RIDGE, width=15).grid(row=4, column=1)
        self.e3=tkinter.Entry(master)
        self.e3.grid(row=4, column=2)

        self.labelAct=tkinter.Label(master, text="Poziom aktywności", font=("Helvetica", 14), bg="LemonChiffon2",
                                    borderwidth=5, relief=tkinter.RIDGE, width=15).grid(row=5, column=1, pady=10)
        self.variable2=tkinter.StringVar(master)
        self.variable2.set(act[0])
        self.opac=tkinter.OptionMenu(master, self.variable2, *act)
        self.opac.config(bg="LemonChiffon2")
        self.opac.grid(row=5, column=2)

        self.labelBal=tkinter.Label(master, font="Helvetica", bg="LemonChiffon2")
        self.labelBal.grid(row=7, column=1)

        self.buttonOk=tkinter.Button(master, text="Oblicz", font="Helvetica", bg="LemonChiffon3", borderwidth=5, relief=tkinter.RIDGE, command=lambda:self.count(self.variable1.get(), float(self.e1.get()), float(self.e2.get()), float(self.e3.get()), self.variable2.get())).grid(row=6, column=1)
        self.buttonBack=tkinter.Button(master, text="Wyjdź", font="Helvetica", bg="LemonChiffon3", borderwidth=5, relief=tkinter.RIDGE, command=lambda :self.back()).grid(row=6, column=2)

    def count(self, gender, weight, height, age, activity):
        try:
            if(gender=="mężczyzna"):
                balance=9.99*weight+6.25*height-4.92*age+5
                if(activity==act[0]):
                    balance=1.2 * balance
                elif(activity==act[1]):
                    balance=1.4 * balance
                elif(activity==act[2]):
                    balance=1.6 * balance
                elif(activity==act[3]):
                    balance=1.8 * balance
                else:
                    balance=1.9 * balance
            else:
                balance = 9.99 * weight + 6.25 *height - 4.92 * age
                balance-=161
                if (activity == act[0]):
                    balance = 1.2 * balance
                elif (activity == act[1]):
                    balance = 1.3 * balance
                elif (activity == act[2]):
                    balance = 1.5 * balance
                elif (activity == act[3]):
                    balance = 1.7 * balance
                else:
                    balance = 1.9 * balance
            balance=float("{:.2f}".format(float(balance)))
            info="Twoje zapotrzebowanie kaloryczne to: " +str(balance)+"kcal"
            self.labelBal.config(text=info)
        except:
            print("Błędne dane")

    def back(self):
        self.master.withdraw()
        toplevel = tkinter.Toplevel(self.master)
        toplevel.config(bg="wheat1")
        toplevel.resizable(width=None, height=None)
        app = MainWindow(toplevel)



root = tkinter.Tk()
root.title("Projekt")
root.resizable(width=None, height=None)
root.config(bg="wheat1")
cls = MainWindow(root)
root.mainloop()