import tkinter
from tkinter import ttk

from PActivity import Activity
from PInfo import *
from PEvent import *
from PMeal import *

window_main=tkinter.Tk()
inf=Info()
inf.prepareDatabase()
inf.prepareTemps("spalono.txt")
inf.prepareTemps("przyjeto.txt")

food=inf.productsList()
sports=inf.sportsList()

window=tkinter.Toplevel()


def createMainWindow():
    window.geometry("1050x500")
    window.title("PROJEKT")

    tkinter.Label(window, text=inf.nameInfo(), font=("Forte", 24)).grid(row=1, column=1)
    tkinter.Label(window, text=inf.getDate(), font=("Forte", 24)).grid(row=2, column=1)
    tkinter.Label(window, text=inf.chooseQuote(), font=("Forte")).grid(row=3, column=1)

    today=datetime.datetime.now()
    template=str(today.day)+"."+str(today.month)+"."+str(today.year)

    tkinter.Label(window, text=inf.getTodaysPlan(template), font=("Forte")).grid(row=1, column=2)
    button_add_event=tkinter.Button(window, text="Dodaj wydarzenie", font=("Forte"), command=lambda :[ addEventWindow(), window.destroy()]).grid(row=4, column=1)
    button_shopping_list=tkinter.Button(window, text="Moja lista zakupów", font="Forte", command=lambda:[listDisplayWindow()]).grid(row=5, column=1)
    button_balance=tkinter.Button(window, text="Bilans kaloryczny", font="Forte", command=lambda:[balanceDisplayWindow()]).grid(row=4, column=2)
    button_choose_date=tkinter.Button(window, text="Przejdź do daty", font="Forte", command=lambda:chosenDateWindow()).grid(row=5, column=2)

def addEventWindow():
    window1=tkinter.Toplevel()
    window1.geometry("400x200")
    window1.title("Dodawanie wydarzenia")
    tkinter.Label(window1, text="Godzina", font=("Forte")).grid(row=1, column=1)
    tkinter.Label(window1, text="Data", font=("Forte")).grid(row=2, column=1)
    tkinter.Label(window1, text="Opis", font=("Forte")).grid(row=3, column=1)
    e1=tkinter.Entry(window1, font=("Forte"))
    e1.grid(row=1, column=3)
    e2=tkinter.Entry(window1, font=("Forte"))
    e2.grid(row=2, column=3)
    e3=tkinter.Entry(window1, font=("Forte"))
    e3.grid(row=3, column=3)
    button_ok = tkinter.Button(window1, text="OK", font="Forte",
                               command=lambda: [addEvent(e1.get(), e2.get(), e3.get())]).grid(row=4, column=1)
    window1.mainloop()


def addEvent(time, date, description):
    temp_date = date.split("-")
    temp_time = time.split(":")
    date = datetime.datetime(int(temp_date[2]), int(temp_date[1]), int(temp_date[0]), int(temp_time[0]),
                             int(temp_time[1]))
    ev=Event()
    ev.setDate(date)
    ev.setDescription(description)
    inf.saveEvent(ev)
    #createMainWindow()
    #window.mainloop()

def listDisplayWindow():
    sl=ShoppingList()
    sl.setList(inf.readShoppingList())
    window2 = tkinter.Toplevel()
    window2.geometry("400x300")
    window2.title("Moja lista zakupów")
    tkinter.Label(window2, font="Forte", text=sl.display()).grid(row=1, column=1)
    button_add_to_list=tkinter.Button(window2, text="Dodaj", font="Forte", command=lambda:shoppingListAddWindow()).grid(row=1, column=2)
    button_clear=tkinter.Button(window2, text="Wyczyść", font="Forte", command=lambda:clearShoppingList()).grid(row=2, column=2)

def shoppingListAddWindow():
    window3=tkinter.Toplevel()
    window3.geometry("400x300")
    window3.title("Dodawanie produktu")
    tkinter.Label(window3, text="Dodawanie produktów do listy zakupów: ", font="Forte").grid(row=1, column=1)
    e1=tkinter.Entry(window3, font=("Forte", 24))
    e1.grid(row=2, column=1)
    button_ok=tkinter.Button(window3, text="Dodaj", font="Forte", command=lambda:[addToShoppingList(e1.get())]).grid(row=3, column=1)

def addToShoppingList(product):
    sl=ShoppingList()
    sl.setList(inf.readShoppingList())
    sl.addProduct(product)
    inf.saveShoppingList(sl)
    #listDisplayWindow()

def clearShoppingList():
    sl=ShoppingList()
    sl.clearList()
    inf.saveShoppingList(sl)
    listDisplayWindow()

def balanceDisplayWindow():
    #print(inf.getEaten())
    window4=tkinter.Toplevel()
    window4.geometry("400x300")
    window4.title("Bilans kaloryczny")

    tkinter.Label(window4, text="Bilans na dziś", font="Forte").grid(row=1, column=2)
    tkinter.Label(window4, text="Przyjęto", font="Forte").grid(row=2, column=1)
    tkinter.Label(window4, text="Spalono", font="Forte").grid(row=3, column=1)
    tkinter.Label(window4, text="łącznie", font="Forte").grid(row=4, column=1)

    tkinter.Label(window4, font="Forte", text=inf.getEaten()).grid(row=2, column=2)
    tkinter.Label(window4, font="Forte", text=inf.getBurnt()).grid(row=3, column=2)

    eb=EnergyBalance()
    if(inf.checkDate(inf.getDate())==False):
        eb.setCalAmount(0)
        inf.saveBalance(eb)
    else:
        eb.setCalAmount(inf.readBalance())

    sum=float(inf.getEaten())+float(inf.getBurnt())

    tkinter.Label(window4, font="Forte", text=str(sum)).grid(row=4, column=2)

    button_add_meal=tkinter.Button(window4, text="Dodaj posiłek", font="Forte", command=lambda:[productsDisplayWindow()]).grid(row=5, column=1)
    button_add_activity=tkinter.Button(window4, text="Dodaj aktywność", font="Forte", command=lambda:[activityDisplayWindow()]).grid(row=5, column=2)


def productsDisplayWindow():
    window5=tkinter.Toplevel()
    window5.title("Dodawanie posiłku")
    window5.geometry("400x300")

    tkinter.Label(window5, text="Produkt", font=("Forte", 24)).grid(row=1, column=1)
    variable1=tkinter.StringVar(window5)
    variable1.set(food[0])
    pp = tkinter.OptionMenu(window5, variable1, *food)
    pp.grid(row=2, column=1)
    pp.config(font=("Forte"))

    tkinter.Label(window5, text="Ilość w gramach", font=("Forte")).grid(row=3, column=1)
    e1=tkinter.Entry(window5, font=("Forte"))
    e1.grid(row=3, column=2)

    button_ok=tkinter.Button(window5, text="OK", font="Forte", command=lambda:[addToBalance(str(variable1.get()), e1.get())]).grid(row=4, column=1)
    button_manual = tkinter.Button(window5, text="Wprowdź ręcznie", font="Forte", command =lambda:manualWindow()).grid(row=4, column=2)

def addToBalance(product, grams):
    record=product+grams
    print(record)
    ml=Meal()
    ml.addIngredient(record)
    calories=ml.countCalories()
    eb=EnergyBalance()
    total=inf.readBalance()+calories
    print(total)
    eb.setCalAmount(total)
    inf.saveBalance(eb)
    inf.saveEaten(calories)

def manualWindow():
    window6=tkinter.Toplevel()
    window6.title("Wprowadź dane")
    window6.geometry("400x300")

    tkinter.Label(window6, text="Podaj ilość", font=("Forte", 24)).grid(row=1, column=1)

    e1=tkinter.Entry(window6, font="Forte")
    e1.grid(row=2, column=1)
    tkinter.Label(window6, text="kcal", font="Forte").grid(row=2, column=2)

    button_ok=tkinter.Button(window6, text="OK", font="Forte", command=lambda:addCalories(float(e1.get()))).grid(row=3, column=1)

def addCalories(amount):
    e=EnergyBalance()
    e.setCalAmount(amount)
    inf.saveBalance(e)
    inf.saveEaten(amount)

def chosenDateWindow():
    window7=tkinter.Toplevel()
    window7.title("Wyszukiwanie")
    window7.geometry("300x600")

    tkinter.Label(window7, text="Podaj datę", font="Forte").grid(row=1, column=1)
    e1=tkinter.Entry(window7, font="Forte")
    e1.grid(row=1, column=2)

    button_ok=tkinter.Button(window7, text="OK", font="Forte", command=lambda:getPlan(e1.get())).grid(row=2, column=2)
    sep=ttk.Separator(window7, orient="horizontal")
    sep.grid(row=3, columnspan=10, ipadx=100)

    days_plan=tkinter.Label(window7, font="Forte")
    days_plan.grid(row=4, column=1)

    def getPlan(date):
        temp=date.split("-")
        chosenDate=temp[0]+"."+temp[1]+"."+temp[2]
        plan=inf.getTodaysPlan(chosenDate)
        days_plan.config(text=plan)

def activityDisplayWindow():
    window8=tkinter.Toplevel()
    window8.geometry("400x300")
    window8.title("Dodawanie aktywności")

    tkinter.Label(window8, font="Forte", text="Rodzaj sportu").grid(row=1, column=1)
    variable1 = tkinter.StringVar(window8)
    variable1.set(sports[0])
    pp = tkinter.OptionMenu(window8, variable1, *sports)
    pp.grid(row=2, column=1)
    pp.config(font=("Forte"))

    tkinter.Label(window8, text="Czas trwania w minutach", font=("Forte")).grid(row=3, column=1)
    e1 = tkinter.Entry(window8, font=("Forte"))
    e1.grid(row=3, column=2)

    button_ok = tkinter.Button(window8, text="OK", font="Forte",
                               command=lambda: [addActivity(str(variable1.get()), e1.get())]).grid(row=4, column=1)

def addActivity(activity, time):
    act=activity+time
    print(act)
    at=Activity()
    at.addActivity(act)
    calories=at.countCalories()
    eb=EnergyBalance()
    eb.setCalAmount(inf.readBalance()+calories)
    inf.saveBalance(eb)
    inf.saveBurnt(calories)

createMainWindow()
window_main.mainloop()











