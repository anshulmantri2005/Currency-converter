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
cor5 = "#9467bd	"    #PURPLE
cor6 = "#708090	"    #SLATEGRAY

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
window.mainloop()
