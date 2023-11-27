import tkinter as tk
from tkinter import *

class prisma_segitiga_ilhamFix:
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

        #Label input
        alas = Label(mainFrame, text="Alas:")
        alas.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        tinggi = Label(mainFrame, text="Tinggi:")
        tinggi.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        Tp = Label(mainFrame, text="Tinggi Prisma:")
        Tp.grid(row=3, column=0, sticky=W, padx=5, pady=5)
        sisi1 = Label(mainFrame, text="Sisi 1:")
        sisi1.grid(row=4, column=0, sticky=W, padx=5, pady=5)
        sisi2 = Label(mainFrame, text="Sisi 2:")
        sisi2.grid(row=5, column=0, sticky=W, padx=5, pady=5)
        sisi3 = Label(mainFrame, text="Sisi 3:")
        sisi3.grid(row=6, column=0, sticky=W, padx=5, pady=5)

        # Textbox input
        self.txtalas = Entry(mainFrame)
        self.txtalas.grid(row=1, column=1)
        self.txttinggi = Entry(mainFrame)
        self.txttinggi.grid(row=2, column=1)
        self.txtTp = Entry(mainFrame)
        self.txtTp.grid(row=3, column=1)
        self.txtsisi1 = Entry(mainFrame)
        self.txtsisi1.grid(row=4, column=1)
        self.txtsisi2 = Entry(mainFrame)
        self.txtsisi2.grid(row=5, column=1)
        self.txtsisi3 = Entry(mainFrame)
        self.txtsisi3.grid(row=6, column=1)

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
        alas = float(self.txtalas.get())
        tinggi = float(self.txttinggi.get())
        Tp = float(self.txtTp.get())
        sisi1 = float(self.txtsisi1.get())
        sisi2 = float(self.txtsisi2.get())
        sisi3 = float(self.txtsisi3.get())

        L = round(((2*(1/2*alas*tinggi)) + ((sisi1 + sisi2 + sisi3)*Tp)),2)
        V = round(((1/2*alas*tinggi)*Tp),2)

        self.txtVolume.delete(0,END)
        self.txtVolume.insert(END,V)
        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END,L)

    def onKeluar(self):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = prisma_segitiga_ilhamFix(root, "Program Bola")
    root.mainloop() 