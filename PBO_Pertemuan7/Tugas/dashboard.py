import tkinter as tk
from tkinter import Menu

from googletrans import Translator
from balok_ilhamFix import *
from bola_ilhamFix import *
from kerucut_ilhamFix import *
from kubus_ilhamFix import *
from limas_segiempat_ilhamFix import *
from limas_segitiga_ilhamFix import *
from prisma_segitiga_ilhamFix import *
from tabung_ilhamFix import *
from Translator import *

# root window
root = tk.Tk()
root.title('Menu Demo')
#root.attributes('-fullscreen', True)
root.geometry("900x400")
# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create a menu
file_menu = Menu(menubar)
app_menu = Menu(menubar)
data_menu = Menu(menubar)

# add a menu item to the menu
file_menu.add_command(label='File Open', command=root.destroy)

file_menu.add_command(label='Exit', command=root.destroy)

app_menu.add_command(label='App Bola', command= lambda: new_window("Luas dan Volume Bola", bola_ilhamFix))
app_menu.add_command(label='App Balok', command= lambda: new_window("Luas dan Volume Balok", balok_ilhamFix))
app_menu.add_command(label='App Krucut', command= lambda: new_window("Luas dan Volume Kerucut", kerucut_ilhamFix))
app_menu.add_command(label='App Kubus', command= lambda: new_window("Luas dan Volume Kubus", kubus_ilhamFix))
app_menu.add_command(label='App Limas Segiempat', command= lambda: new_window("Luas dan Volume Limas Segiempat", limas_segiempat_ilhamFix))
app_menu.add_command(label='App Limas Segitiga', command= lambda: new_window("Luas dan Volume Limas Segitiga", limas_segitiga_ilhamFix))
app_menu.add_command(label='App Prisma Segitiga', command= lambda: new_window("Luas dan Volume Prisma Segitiga", prisma_segitiga_ilhamFix))
app_menu.add_command(label='App Tabung', command= lambda: new_window("Luas dan Volume Tabung", tabung_ilhamFix))

#add translator
data_menu.add_command(label='Translator', command= lambda: new_window("Luas dan Volume Tabung", Translator))


def new_window( number, _class):
    new = tk.Toplevel()
    new.transient()
    new.grab_set()
    _class(new, number)

# add the File menu to the menubar
menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="App", menu=app_menu)
menubar.add_cascade(label="Translator", menu=data_menu)
    
root.mainloop()