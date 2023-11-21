import tkinter as tk
from tkinter import *
from math import pi

class test_class:
    def __init__(self, parent, title):
        self.parent = parent       
        #self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
    
        nama = Label(mainFrame, text="MUHAMMAD ILHAM RAMDHANI")
        nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        #Label jari jari
        jari_jari = Label(mainFrame, text="jari jari:")
        jari_jari.grid(row=1, column=0, sticky=W, padx=5, pady=5)

        # Textbox jari jari
        self.txtjari_jari = Entry(mainFrame)
        self.txtjari_jari.grid(row=1, column=1)

        #Button
        self.hitung_button = Button(mainFrame, text="Hitung", command=self.onHitung)
        self.hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

        #Output label Luas
        self.luas = Label(mainFrame, text="Luas :")
        self.luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

        #Output label Volume
        self.volume = Label(mainFrame, text="volume :")
        self.volume.grid(row=4, column=0, sticky=W, padx=5, pady=5)

        #Output Textbox Luas
        self.txtLuas= Entry(mainFrame)
        self.txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

        #output Textbox Volume
        self.txtVolume = Entry(mainFrame)
        self.txtVolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)

    # fungsi "onHitung" berfungsi untuk menghitung luas persegi panjang  
    def onHitung(self):
        r = float(self.txtjari_jari.get())
        L = round((4 * pi * r**2),2)
        V = round((4/3 * pi * r**3),2)
        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END,str(L))
        self.txtVolume.delete(0,END)
        self.txtVolume.insert(END,V)

    def onKeluar(self):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = test_class(root, "Program Bola")
    root.mainloop() 