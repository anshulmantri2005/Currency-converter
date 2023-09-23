# importing everything from tkinter
from tkinter import *

# importing ttk widgets from tkinter
from tkinter import ttk
from PIL import Image,ImageTk
import json
import requests

cor0 = "#FFFFFF"     #WHITE
cor1 = "#333333"     #BLACK
cor2 = "#E85051"     #RED
cor3 = "#57FF53"     #GREEN
cor4 = "#0000ff"     #BLUE


# creating the main window
window = Tk()
# this gives the window the width(310), height(320) and the position(center)
window.geometry('300x320+500+200')
# this is the title for the window
window.title('Currency Converter')
window.configure(bg=cor0)
# this will make the window not resizable, since height and width is TRUE
window.resizable(height=TRUE, width=TRUE)

#frame
top = Frame(window,width=300,height=60,bg=cor3)
top.grid(row=0,column=0)

main = Frame(window,width=300,height=260,bg=cor0)
main.grid(row=1,column=0)

#logo of the currency converter
icon = Image.open("icon2.jpg")
icon = icon.resize((40,40))
icon = ImageTk.PhotoImage(icon)
#we create name of this gui 
app_name = Label(top,image=icon, compound=LEFT, text="Currency Converter",height=5,padx=9,pady=25,anchor=CENTER,font=("arial 16 bold"),bg=cor3,fg=cor1)
app_name.place(x=-9,y=0)


#main frame
result = Label(main,text=" ",width=16,height=2,pady=7,relief="solid",anchor=CENTER,font=("Ivy 15 bold"),bg=cor0,fg=cor2)
result.place(x=50,y=10)
#NAME AND CODE OF DIFFERENT COUNTRY CURRENCY
currency = ["INR","CNY","EUR","JPY","PKR","RUB","USD","BDT","KZT","OMR"]

from_lable = Label( main,text="FROM",width=8,height=1,pady=0,padx=0,relief="solid",anchor=CENTER,font=("Ivy 10 bold"),bg=cor0,fg=cor2)
from_lable.place(x=63,y=90)

combo1 = ttk.Combobox(main,width=8,justify=CENTER,font=("Ivy 12 bold"))
combo1["values"] = (currency)
combo1.place(x=50,y=115)

to_lable = Label( main,text="TO",width=8,height=1,pady=0,padx=0,relief="solid",anchor=CENTER,font=("Ivy 10 bold"),bg=cor0,fg=cor2)
to_lable.place(x=168,y=90)
combo2 = ttk.Combobox(main,width=8,justify=CENTER,font=("Ivy 12 bold"))
combo2["values"] = (currency)
combo2.place(x=155,y=115)


value = Entry(main,width=22,justify=CENTER,font=("Ivy 12 bold"),relief=SOLID)
value.place(x=50,y=155)

window.mainloop()
