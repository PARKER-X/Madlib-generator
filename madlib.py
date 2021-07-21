from tkinter import *
from tkinter.font import names
root = Tk()

root.geometry("444x444")
root.title("Parker-madlib generator")
ironman = Label(text="Madlib Generator\n Have fun!", font="arial 20 bold")
ironman.pack()

ironman = Label(text = 'Click Any One :', font = 'arial 15 bold').place(x=40, y=80)

def madlib1():
    animals= input("Enter the animals name: ")
    profession = input("Enter the profession: ")
    cloth = input("Enter the name of cloth: ")
    things = input("Enter the name of a thing: ")
    place = input("Enter the name of a place: ")
    name = input("Enter the name: ")
    food = input("Enter the name of yummy food")

    print("hello\n My name is " + name +"my profession is "+profession+"my favourite cloth is " + cloth +" my favourite animal is" + animals +" my favourite place is" + place + "my favourite food is"+ food + +"." )

def madlib2():
    animals= input("Enter the animals name: ")
    profession = input("Enter the profession: ")
    cloth = input("Enter the name of cloth: ")
    things = input("Enter the name of a thing: ")
    place = input("Enter the name of a place: ")
    name = input("Enter the name: ")
    food = input("Enter the name of yummy food")

    print("hello\n My name is " + name +"my profession is "+profession+"my favourite cloth is " + cloth +" my favourite animal is" + animals +" my favourite place is" + place + "my favourite food is"+ food + +"." )

def madlib3():
    animals= input("Enter the animals name: ")
    profession = input("Enter the profession: ")
    cloth = input("Enter the name of cloth: ")
    things = input("Enter the name of a thing: ")
    place = input("Enter the name of a place: ")
    name = input("Enter the name: ")
    food = input("Enter the name of yummy food")

    print("hello\n My name is " + name +"my profession is "+profession+"my favourite cloth is " + cloth +" my favourite animal is" + animals +" my favourite place is" + place + "my favourite food is"+ food  +"." )

ironman = Button(text="The photographer", font="arial 15 bold", command=madlib1 ,bg="ghost white").place(x= 60, y=120)
ironman = Button(text="The Astronaut", font="arial 15 bold", command=madlib2 ,bg="ghost white").place(x= 70, y=180)
ironman = Button(text="The Business - Man", font="arial 15 bold", command=madlib3 ,bg="ghost white").place(x= 80, y=240)
root.mainloop()
