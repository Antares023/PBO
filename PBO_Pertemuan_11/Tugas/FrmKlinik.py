import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Klinik_ilham import obat

class FrmKlinik:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Label
        Label(mainFrame, text='Kode Obat:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txtkdobat = Entry(mainFrame) 
        self.txtkdobat.grid(row=0, column=1, padx=5, pady=5) 
        self.txtkdobat.bind("<Return>",self.onCari) # menambahkan event Enter key

        Label(mainFrame, text='Nama:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5) 

        Label(mainFrame, text='Berat:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtBerat = Entry(mainFrame) 
        self.txtBerat.grid(row=2, column=1, padx=5, pady=5) 
        
        Label(mainFrame, text='Bentuk:').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.txtBentuk = Entry(mainFrame) 
        self.txtBentuk.grid(row=3, column=1, padx=5, pady=5) 
        

        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        self.btnCari = Button(mainFrame, text='Cari', command=self.onCari, width=10)
        self.btnCari.grid(row=3, column=3, padx=5, pady=5)

        columns = ('id', 'kdobat', 'nama', 'berat', 'bentuk')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=80)  # Adjust the width as needed
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtkdobat.delete(0,END)
        self.txtkdobat.insert(END,"")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")       
        self.txtBerat.delete(0,END)
        self.txtBerat.insert(END,"")       
        self.txtBentuk.delete(0,END)
        self.txtBentuk.insert(END,"")       
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data mahasiswa
        dataobat = obat()
        result = dataobat.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        students=[]
        for row_data in result:
            students.append(row_data)

        for student in students:
            self.tree.insert('',END, values=student)
    
    def onCari(self, event=None):
        kdobat = self.txtkdobat.get()
        dataobat = obat()
        res = dataobat.getByKdobat(kdobat)
        rec = dataobat.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txtNama.focus()
        return res
        
    def TampilkanData(self, event=None):
        kdobat = self.txtkdobat.get()
        dataobat = obat()
        res = dataobat.getByKdobat(kdobat)
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,dataobat.nama)
        self.txtBerat.delete(0,END)
        self.txtBerat.insert(END,dataobat.berat)
        self.txtBentuk.delete(0,END)
        self.txtBentuk.insert(END,dataobat.bentuk) 
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        kdobat = self.txtkdobat.get()
        nama = self.txtNama.get()
        berat = self.txtBerat.get()
        bentuk = self.txtBentuk.get()
        
        dataobat = obat()
        dataobat.kdobat = kdobat
        dataobat.nama = nama
        dataobat.berat = berat
        dataobat.bentuk = bentuk
        if(self.ditemukan==True):
            res = dataobat.updateByKdobat(kdobat)
            ket = 'Diperbarui'
        else:
            res = dataobat.simpan()
            ket = 'Disimpan'
            
        rec = dataobat.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        kdobat = self.txtkdobat.get()
        dataobat = obat()
        dataobat.nim = kdobat
        if(self.ditemukan==True):
            res = dataobat.deleteByKdobat(kdobat)
            rec = dataobat.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FrmKlinik(root, "Aplikasi Klinik Obat Ilham")
    root.mainloop() 