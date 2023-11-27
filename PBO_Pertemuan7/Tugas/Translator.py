from tkinter import *
from googletrans import Translator

class FrmTranslator:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("900x400")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        # pasang Label
        Label(mainFrame, text='Masukkan teks:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Terjemahan Jepang:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Terjemahan Jawa:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Terjemahan Sunda:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        
        # pasang textbox
        self.txtSumber = Entry(mainFrame, width=50) 
        self.txtSumber.grid(row=0, column=1, padx=5, pady=5)

        self.txtHasil = Entry(mainFrame, width=50) 
        self.txtHasil.grid(row=2, column=1, padx=5, pady=5)
        self.txtHasil2 = Entry(mainFrame, width=50) 
        self.txtHasil2.grid(row=3, column=1, padx=5, pady=5)
        self.txtHasil3 = Entry(mainFrame, width=50) 
        self.txtHasil3.grid(row=4, column=1, padx=5, pady=5)

        # Pasang Button
        self.btnTranslate = Button(mainFrame, text='Translate!',
            command=self.onTranslate)
        self.btnTranslate.grid(row=1, column=1, padx=5, pady=5) 

    def onTranslate(self):
        # membuat instance object
        penterjemah = Translator()

        # menterjemahkan
        hasil = penterjemah.translate(self.txtSumber.get(), src='id', dest='ja') 
        hasil2 = penterjemah.translate(self.txtSumber.get(), src='id', dest='jw') 
        hasil3 = penterjemah.translate(self.txtSumber.get(), src='id', dest='su') 
       
        # menampilkan hasil terjemahan
        self.txtHasil.insert(END,hasil.text)
        self.txtHasil2.insert(END,hasil2.text)
        self.txtHasil3.insert(END,hasil3.text)

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmTranslator(root, "Program Translator")
    root.mainloop() 