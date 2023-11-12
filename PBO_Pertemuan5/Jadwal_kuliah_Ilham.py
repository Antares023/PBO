from email import message
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

def tambah_jadwal():
    nama_file = str(entry_nama_file.get())
    try:
        with open(nama_file, "a") as file:
            data_jadwal = f"[{entry_hari.get()}] | [{entry_jam.get()}] | [{entry_kodeMK.get()}] | [{entry_mata_kuliah.get()}] | [{entry_sks.get()}] | [{entry_dosen.get()}]\n"
            file.write(data_jadwal)
        messagebox.showinfo("Sukses!", "Data Berhasil Disimpan!")
    except Exception as e:
        messagebox.showinfo("Error", "Terjadi Kesalahan!")

def openFile():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read()
    txtarea.insert(END, data)
    tf.close()


app = tk.Tk()
app.title("Aplikasi Jadwal Mata Kuliah")
frame = Frame(app)
frame.pack(padx=40, pady=40)

nama = Label(frame, text="MUHAMMAD ILHAM RAMDHANI (220511113)")
nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Membuat Label
hari = Label(frame, text="Hari:")
hari.grid(row=1, column=0, sticky=W, padx=5, pady=5)
jam = Label(frame, text="Jam:")
jam.grid(row=2, column=0, sticky=W, padx=5, pady=5)
kodeMK = Label(frame, text="Kelas Kuliah:")
kodeMK.grid(row=3, column=0, sticky=W, padx=5, pady=5)
mata_kuliah = Label(frame, text="Mata Kuliah:")
mata_kuliah.grid(row=4, column=0, sticky=W, padx=5, pady=5)
sks = Label(frame, text="Jumlah SKS:")
sks.grid(row=5, column=0, sticky=W, padx=5, pady=5)
dosen = Label(frame, text="Dosen Pengampu:")
dosen.grid(row=6, column=0, sticky=W, padx=5, pady=5)
nama_file = Label(frame, text="Masukkan nama file :")
nama_file.grid(row=7, column=0, sticky=W, padx=5, pady=5)

# Membuat Label untuk textarea
kuliah = Label(frame, text="Jadwal Kuliah:")
kuliah.grid(row=11, column=0, sticky=W, padx=5, pady=5)

# Membuat Entry
entry_hari = Entry(frame)
entry_hari.grid(row=1, column=1)
entry_jam = Entry(frame)
entry_jam.grid(row=2, column=1)
entry_kodeMK = Entry(frame)
entry_kodeMK.grid(row=3, column=1)
entry_mata_kuliah = Entry(frame)
entry_mata_kuliah.grid(row=4, column=1)
entry_sks = Entry(frame)
entry_sks.grid(row=5, column=1)
entry_dosen = Entry(frame)
entry_dosen.grid(row=6, column=1)
entry_nama_file = Entry(frame)
entry_nama_file.grid(row=7, column=1)

entry_hari.delete(0,END)
entry_jam.delete(0,END)
entry_kodeMK.delete(0,END)
entry_mata_kuliah.delete(0,END)
entry_sks.delete(0,END)
entry_dosen.delete(0,END)


# Button
button_save = Button(frame, text="Save Mata Kuliah", command=tambah_jadwal, bg="lightgrey")
button_save.grid(row=8, column=1, sticky=W, padx=5, pady=5)
button_open = Button(frame, text="Open Mata Kuliah", command=openFile, bg="lightgreen")
button_open.grid(row=8, column=0, sticky=W, padx=5, pady=5)

# Text Area
txtarea = Text(frame, width=110, height=15)
txtarea.grid(row=12)

pathh = Entry(frame)
pathh.grid(row=10, column=0)

app.mainloop()