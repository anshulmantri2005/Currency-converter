import tkinter as tk
def display_currency_strength():
    strength_window = tk.Tk()
    strength_window.geometry('670x395')
    strength_window.title('Currency Strength List')
    strength_window.resizable(False, False)  # Disable resizing

    # Set background color to a light beige
    strength_window.configure(bg='#FF00FF')##39FF14

    # Define the currency strength data
    currency_strength_data = '''
    Currency & Symbol              Value In Rs        Value in USD

  #1 Kuwaiti Dinar (KWD)              269.54              3.24
  #2 Bahraini Dinar (BHD)             220.83              2.65
  #3 Omani Rial (OMR)                 216.33              2.60
  #4 Jordanian Dinar (JOD)            117.62              1.41
  #5 British Pound (GBP)              103.29              1.24
  #6 Gibraltar Pound (GIP)            103.27              1.23
  #7 Cayman Island Dollar (KYD)       100.14              1.20
  #8 Swiss Franc (CHF)                 92.99              1.12
  #9 Euro (EUR)                        88.88              1.07
  #10 United States Dollar (USD)       83.29              1.00
    '''

    # Create a title label with a dark blue color
    title_label = tk.Label(strength_window, text="Currency Strength List", font=("Arial", 16, "bold"), bg='#39FF14',
                           fg='red')
    title_label.pack(pady=(10, 10.5))

    # Create a text widget to display the data
    text_widget = tk.Text(strength_window, font=("Courier New", 12), wrap='none', bd=0, height=16)
    text_widget.pack()

    # Insert the currency strength data into the text widget
    text_widget.insert(tk.END, currency_strength_data)

    # Disable editing in the text widget
    text_widget.configure(state='disabled')

    # Function for "Close" button
    def on_close_click():
        strength_window.destroy()

    # Create "Close" button with a dark red color
    close_button = tk.Button(strength_window, text="Close", command=on_close_click, width=10,
                             font=("Arial", 10, "bold"), bg='#FF0000', fg='white')
    close_button.pack(pady=14)

    strength_window.mainloop()


def open_strength_window():
    main_window.destroy()
    display_currency_strength()


# Main window with a blue and orange color scheme
main_window = tk.Tk()
main_window.geometry('400x140')
main_window.title('Main Window')
main_window.resizable(False, False)  # Disable resizing

# Set background color to light blue
main_window.configure(bg='#00008B')

# Label in the main window with a light orange color
label = tk.Label(main_window, text="Click below to get currency strength:", font=("Arial", 14, "bold"), bg='#ADD8E6',
                 fg='black')
label.pack(pady=(30, 20))

# Create "Yes" button in the main window with a dark green color
yes_button = tk.Button(main_window, text="Yes", command=open_strength_window, bg='#008000', fg='white', width=10,
                       font=("Arial", 10, "bold"))
yes_button.pack(side="left", padx=10, pady=10)


# Function for "No" button
def on_no_click():
    main_window.destroy()


# Create "No" button in the main window with a dark red color
no_button = tk.Button(main_window, text="No", command=on_no_click, bg='#FF0000', fg='white', width=10,
                      font=("Arial", 10, "bold"))
no_button.pack(side="right", padx=10, pady=10)

main_window.mainloop()









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
cor5 = "#00F5FF	"    #PURPLE
cor6 = "#708090	"    #SLATEGRAY

# creating the main window
window = Tk()
# this gives the window the width(310), height(320) and the position(center)
window.geometry('300x320+500+200')
# this is the title for the window
window.title('Currency Converter')
window.configure(bg=cor0)
# this will make the window not resizable, since height and width is TRUE
window.resizable(height=FALSE, width=FALSE)

#frame
top = Frame(window,width=300,height=60,bg=cor3)
top.grid(row=0,column=0)

main = Frame(window,width=300,height=260,bg=cor0)
main.grid(row=1,column=0)
def convert():
   #API
    import requests

    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"
    currency_1 = combo1.get()
    currency_2 = combo2.get()
    amount = value.get()

    querystring = {"from": currency_1, "to": currency_2,"amount": amount}
    if currency_2 == "INR":
        symbol = "₹"
    elif currency_2 == "CNY":
        symbol = "¥"
    elif currency_2 == "EUR":
        symbol = "€"
    elif currency_2 == "JPY":
        symbol = "¥"
    elif currency_2 == "PKR":
        symbol = "₨"
    elif currency_2 == "RUB":
        symbol = "₽"
    elif currency_2 == "USD":
        symbol = "$"
    elif currency_2 == "BDT":
        symbol = "৳"
    elif currency_2 == "KZT":
        symbol = "лв"
    elif currency_2 == "OMR":
        symbol = "﷼"
    elif currency_2 == "AED":
        symbol = "د.إ"


    headers = {
        "X-RapidAPI-Key": "329fbc4bc5msh132f4164bed55fap15edfejsne2dd3fc3aaba",
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = json.loads(response.text)
    converted_amount = data["result"]["convertedAmount"]
    formatted = symbol + "{:,.2f}".format(converted_amount)
    result["text"] = formatted

    print(converted_amount, formatted)

#top frame
icon = Image.open("icon2.jpg")
icon = icon.resize((40,40))
icon = ImageTk.PhotoImage(icon)

app_name = Label(top,image=icon, compound=LEFT, text="Currency Converter",height=5,padx=9,pady=25,anchor=CENTER,font=("arial 16 bold"),bg=cor3,fg=cor1)
app_name.place(x=-9,y=0)


#main frame
result = Label(main,text=" ",width=16,height=2,pady=7,relief="solid",anchor=CENTER,font=("Ivy 15 bold"),bg=cor0,fg=cor2)
result.place(x=50,y=10)

#NAME AND CODE OF DIFFERENT COUNTRY CURRENCY
currency = ["INR","CNY","EUR","JPY","PKR","RUB","USD","BDT","KZT","OMR","AED"]

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
#BUTTON CREATE
button = Button(main,text="Convert",width=19,padx=5,height=1,bg=cor2,fg=cor0,font=("Ivy 12 bold"),command=convert)
button.place(x=50,y=210)
window.mainloop()
