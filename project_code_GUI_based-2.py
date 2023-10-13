from currency_converter import CurrencyConverter
import tkinter as tk
from tkinter import ttk

a = CurrencyConverter()

def show_result():
    amount = int(e1.get())
    cur1 = e2.get()
    cur2 = e3.get()
    data = a.convert(amount, cur1, cur2)
    symbol = get_currency_symbol(cur2)

    result_window = tk.Tk()
    result_window.geometry('300x70+600+300')
    result_window.configure(bg='#ADD8E6')  # Set background color to light blue
    result_window.resizable(False, False)  # Disable resizing

    result_label = tk.Label(result_window, text=f"{symbol}{data:.2f}", font="Times 20 bold", bg='#ADD8E6')
    result_label.pack(pady=20)

    result_window.mainloop()

def get_currency_symbol(currency_code):
    currency_symbols = {
        'USD': '$',
        'EUR': '€',
        'JPY': '¥',
        'GBP': '£',
        'AUD': 'A$',
        'CAD': 'C$',
        'CHF': 'CHF',
        'CNY': '¥',
        'SEK': 'kr',
        'NZD': 'NZ$',
        'KRW': '₩',
        'SGD': 'S$',
        'HKD': 'HK$',
        'NOK': 'kr',
        'MXN': 'Mex$',
        'INR': '₹',
        'RUB': '₽',
        'ZAR': 'R',
        'BRL': 'R$',
        'TRY': '₺',
    }
    return currency_symbols.get(currency_code, '')

window = tk.Tk()
window.geometry('620x320+200+200')
window.configure(bg='#ADD8E6')  # Set background color to light blue
window.resizable(False, False)  # Disable resizing

# Calculate center position for label
label_x = (620 - (len("Currency Converter") * 10)) // 2

l1 = tk.Label(window, text="Currency Converter", font="Times 20 bold", bg='#ADD8E6')
l1.place(x=185, y=30)

# Label and Entry for amount
l_amount = tk.Label(window, text="Amount", font="Times 12 bold", bg='#ADD8E6')
l_amount.place(x=10, y=100)
e1 = tk.Entry(window, width=15, font=("Ivy 12 bold"))  # Adjusted width here
e1.place(x=70, y=100)

# Entry for currency to convert from
e2 = ttk.Combobox(window, width=15, justify='center', font=("Ivy 12 bold"))  # Adjusted width here
e2["values"] = ("INR","USD", "EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD", "KRW", "SGD", "HKD", "NOK", "MXN", "RUB", "ZAR", "BRL", "TRY")
e2.place(x=255, y=100)

# Entry for currency to convert to
e3 = ttk.Combobox(window, width=15, justify='center', font=("Ivy 12 bold"))  # Adjusted width here
e3["values"] = ("INR","USD", "EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD", "KRW", "SGD", "HKD", "NOK", "MXN", "RUB", "ZAR", "BRL", "TRY")
e3.place(x=440, y=100)

# Labels
l2 = tk.Label(window, text="From", font="Times 12 bold", bg='#ADD8E6')
l2.place(x=210, y=100)
l3 = tk.Label(window, text="To", font="Times 12 bold", bg='#ADD8E6')
l3.place(x=420, y=100)

b1 = tk.Button(window, text="Convert", command=show_result, font="Times 14 bold")
b1.place(x=235, y=200, width=150, height=40)  # Adjusted width and height here

window.mainloop()
