from currency_converter import CurrencyConverter
import tkinter as tk
a = CurrencyConverter()

window = tk.Tk()
# this gives the window the width(310), height(320) and the position(center)
window.geometry('500x420+500+200')
def Converted():
    amount = int(e1.get())
    cur1 = e2.get()
    cur2 = e3.get()
    data = a.convert(amount,cur1,cur2)
    l5 = tk.Label(window,text= data).place(x=230,y=290)


l1 = tk.Label(window,text="Currency Converter", font= "Times 20 bold").place( x=130,y=30)
l2 = tk.Label(window,text="Enter amount here : ",font= "Times 18 bold").place( x=69,y=80)
e1 = tk.Entry(window)
l3 = tk.Label(window,text="Enter currency :",font= "Times 18 bold").place(x=106,y=130)
e2 = tk.Entry(window)
l4 = tk.Label(window,text="Enter req currency :",font= "Times 18 bold").place(x=66,y=180)
e3 = tk.Entry(window)
b1 = tk.Button(window,text="Convert", command= Converted).place(x=230,y=240)
e1.place(x=300,y=90)
e2.place(x=300,y=140)
e3.place(x=300,y=190)
window.mainloop()
