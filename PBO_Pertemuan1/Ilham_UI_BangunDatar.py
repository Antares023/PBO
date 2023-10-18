import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk

def hitung_persegi():
    sisi = float(sisi_persegi_entry.get())
    luas = sisi ** 2
    keliling = 4 * sisi
    hasil_persegi_label.config(text=f"Luas: {luas:.2f}, Keliling: {keliling:.2f}")

def hitung_persegiPanjang():
    panjang = float(panjang_persegiPanjang_entry.get())
    lebar = float(lebar_persegiPanjang_entry.get())
    luas = panjang * lebar
    keliling = 2 *(panjang + lebar)
    hasil_persegiPanjang_label.config(text = f"Luas: {luas:.2f}, Keliling: {keliling:.2f}")

def hitung_jajarGenjang():
    sisi1 = float(sisi1_jajarGenjang_entry.get())
    sisi2 = float(sisi2_jajarGenjang_entry.get())
    tinggi = float(tinggi_jajarGenjang_entry.get())
    luas = sisi1 * tinggi
    keliling = (sisi1 * 2) + (sisi2 * 2)
    hasil_jajarGenjang_label.config(text = f"Luas: {luas:.2f}, Keliling: {keliling:.2f}")

def hitung_segitiga():
    alas = float(alas_segitiga_entry.get())
    tinggi = float(tinggi_segitiga_entry.get())
    luas = 0.5 * (alas * tinggi)
    sisi = float(sisi_segitiga_entry.get())
    keliling = alas + sisi + sisi
    hasil_segitiga_label.config(text=f"Luas: {luas:.2f}, Keliling: {keliling:.2f}")

def hitung_belahKetupat():
    diagonal1 = float(diagonal1_belahKetupat_entry.get())
    diagonal2 = float(diagonal2_belahKetupat_entry.get())
    sisi = float(sisi_belahKetupat_entry.get())
    luas = (diagonal1 * diagonal2)/2
    keliling = sisi * 4
    hasil_belahKetupat_label.config(text = f"Luas: {luas:.2f}, Keliling: {keliling:.2f}")

def hitung_layang():
    sisiA = float(sisiA_layang_entry.get())
    sisiB = float(sisiB_layang_entry.get())
    diagonal1 = float(diagonal1_layang_entry.get())
    diagonal2 = float(diagonal2_layang_entry.get())
    luas = (diagonal1 * diagonal2)/2
    keliling = (sisiA * 2) + (sisiB * 2)
    hasil_layang_label.config(text = f"Luas: {luas:.2f}, Keliling: {keliling:.2f}")

def hitung_trapesium():
    sisiA = float(sisiA_trapesium_entry.get())
    sisiB = float(sisiB_trapesium_entry.get())
    sisiC = float(sisiC_trapesium_entry.get())
    sisiD = float(sisiD_trapesium_entry.get())
    tinggi = float(tinggi_trapesium_entry.get())
    luas = ((sisiA + sisiB)* tinggi)/2
    keliling = sisiA + sisiB + sisiC + sisiD
    hasil_trapesium_label.config(text = f"Luas: {luas:.2f}, Keliling: {keliling:.2f}")

def hitung_lingkaran():
    jari_jari = float(jari_jari_lingkaran_entry.get())
    luas = 3.14 * jari_jari ** 2
    keliling = 2 * 3.14 * jari_jari
    hasil_lingkaran_label.config(text=f"Luas: {luas:.2f}, Keliling: {keliling:.2f}")

root = tk.Tk()
root.title("Kalkulator Luas dan Keliling Bangun Datar")
root.geometry("600x500")

style = ThemedStyle(root)
style.set_theme("equilux")

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

frame_persegi = ttk.Frame(notebook)
frame_persegiPanjang = ttk.Frame(notebook)
frame_jajarGenjang = ttk.Frame(notebook)
frame_segitiga = ttk.Frame(notebook)
frame_belahKetupat = ttk.Frame(notebook)
frame_layang = ttk.Frame(notebook)
frame_trapesium = ttk.Frame(notebook)
frame_lingkaran = ttk.Frame(notebook)

notebook.add(frame_persegi, text="Persegi")
notebook.add(frame_persegiPanjang, text="Persegi panjang")
notebook.add(frame_jajarGenjang, text="Jajar Genjang")
notebook.add(frame_segitiga, text="Segitiga")
notebook.add(frame_belahKetupat, text="Belah Ketupat")
notebook.add(frame_layang, text="Layang")
notebook.add(frame_trapesium, text="Trapesium")
notebook.add(frame_lingkaran, text="Lingkaran")

# Persegi
persegi_label = ttk.Label(frame_persegi, text="Masukkan panjang sisi:")
persegi_label.pack(pady=10)
sisi_persegi_entry = ttk.Entry(frame_persegi)
sisi_persegi_entry.pack()
hitung_persegi_button = ttk.Button(frame_persegi, text="Hitung", command=hitung_persegi)
hitung_persegi_button.pack(pady=10)
hasil_persegi_label = ttk.Label(frame_persegi, text="")
hasil_persegi_label.pack()

# Persegi Panjang
persegiPanjang_label = ttk.Label(frame_persegiPanjang, text="Masukkan panjang :")
persegiPanjang_label.pack(pady=10)
panjang_persegiPanjang_entry = ttk.Entry(frame_persegiPanjang)
panjang_persegiPanjang_entry.pack()
persegiPanjang_label = ttk.Label(frame_persegiPanjang, text="Masukkan lebar :")
persegiPanjang_label.pack(pady=10)
lebar_persegiPanjang_entry = ttk.Entry(frame_persegiPanjang)
lebar_persegiPanjang_entry.pack()
hitung_persegiPanjang_button = ttk.Button(frame_persegiPanjang, text="Hitung", command=hitung_persegiPanjang)
hitung_persegiPanjang_button.pack(pady=10)
hasil_persegiPanjang_label = ttk.Label(frame_persegiPanjang, text="")
hasil_persegiPanjang_label.pack()

# Jajar Genjang
jajarGenjang_label = ttk.Label(frame_jajarGenjang, text="Masukkan Sisi 1 :")
jajarGenjang_label.pack(pady=10)
sisi1_jajarGenjang_entry = ttk.Entry(frame_jajarGenjang)
sisi1_jajarGenjang_entry.pack()
jajarGenjang_label = ttk.Label(frame_jajarGenjang, text="Masukkan Sisi 2 :")
jajarGenjang_label.pack(pady=10)
sisi2_jajarGenjang_entry = ttk.Entry(frame_jajarGenjang)
sisi2_jajarGenjang_entry.pack()
jajarGenjang_label = ttk.Label(frame_jajarGenjang, text="Masukkan Tinggi :")
jajarGenjang_label.pack(pady=10)
tinggi_jajarGenjang_entry = ttk.Entry(frame_jajarGenjang)
tinggi_jajarGenjang_entry.pack()
hitung_jajarGenjang_button = ttk.Button(frame_jajarGenjang, text="Hitung", command=hitung_jajarGenjang)
hitung_jajarGenjang_button.pack(pady=10)
hasil_jajarGenjang_label = ttk.Label(frame_jajarGenjang, text="")
hasil_jajarGenjang_label.pack()

# Segitiga
segitiga_label = ttk.Label(frame_segitiga, text="Masukkan panjang alas:")
segitiga_label.pack(pady=10)
alas_segitiga_entry = ttk.Entry(frame_segitiga)
alas_segitiga_entry.pack()
tinggi_segitiga_label = ttk.Label(frame_segitiga, text="Masukkan tinggi:")
tinggi_segitiga_label.pack(pady=5)
tinggi_segitiga_entry = ttk.Entry(frame_segitiga)
tinggi_segitiga_entry.pack()
sisi_segitiga_label = ttk.Label(frame_segitiga, text="Masukkan panjang sisi:")
sisi_segitiga_label.pack(pady=5)
sisi_segitiga_entry = ttk.Entry(frame_segitiga)
sisi_segitiga_entry.pack()
hitung_segitiga_button = ttk.Button(frame_segitiga, text="Hitung", command=hitung_segitiga)
hitung_segitiga_button.pack(pady=10)
hasil_segitiga_label = ttk.Label(frame_segitiga, text="")
hasil_segitiga_label.pack()

# Belah Ketupat
belahKetupat_label = ttk.Label(frame_belahKetupat, text="Masukkan diagonal 1 :")
belahKetupat_label.pack(pady=10)
diagonal1_belahKetupat_entry = ttk.Entry(frame_belahKetupat)
diagonal1_belahKetupat_entry.pack()
belahKetupat_label = ttk.Label(frame_belahKetupat, text="Masukkan diagonal 2 :")
belahKetupat_label.pack(pady=10)
diagonal2_belahKetupat_entry = ttk.Entry(frame_belahKetupat)
diagonal2_belahKetupat_entry.pack()
belahKetupat_label = ttk.Label(frame_belahKetupat, text="Masukkan sisi :")
belahKetupat_label.pack(pady=10)
sisi_belahKetupat_entry = ttk.Entry(frame_belahKetupat)
sisi_belahKetupat_entry.pack()
hitung_belahKetupat_button = ttk.Button(frame_belahKetupat, text="Hitung", command=hitung_belahKetupat)
hitung_belahKetupat_button.pack(pady=10)
hasil_belahKetupat_label = ttk.Label(frame_belahKetupat, text="")
hasil_belahKetupat_label.pack()

# Layang Layang
layang_label = ttk.Label(frame_layang, text="Masukkan sisi Atas :")
layang_label.pack(pady=10)
sisiA_layang_entry = ttk.Entry(frame_layang)
sisiA_layang_entry.pack()
layang_label = ttk.Label(frame_layang, text="Masukkan sisi Bawah :")
layang_label.pack(pady=10)
sisiB_layang_entry = ttk.Entry(frame_layang)
sisiB_layang_entry.pack()
layang_label = ttk.Label(frame_layang, text="Masukkan diagonal 1 :")
layang_label.pack(pady=10)
diagonal1_layang_entry = ttk.Entry(frame_layang)
diagonal1_layang_entry.pack()
layang_label = ttk.Label(frame_layang, text="Masukkan diagonal 2 :")
layang_label.pack(pady=10)
diagonal2_layang_entry = ttk.Entry(frame_layang)
diagonal2_layang_entry.pack()
hitung_layang_button = ttk.Button(frame_layang, text="Hitung", command=hitung_layang)
hitung_layang_button.pack(pady=10)
hasil_layang_label = ttk.Label(frame_layang, text="")
hasil_layang_label.pack()

# Trapesium
trapesium_label = ttk.Label(frame_trapesium, text="Masukkan sisi Alas :")
trapesium_label.pack(pady=10)
sisiA_trapesium_entry = ttk.Entry(frame_trapesium)
sisiA_trapesium_entry.pack()
trapesium_label = ttk.Label(frame_trapesium, text="Masukkan sisi Atas :")
trapesium_label.pack(pady=10)
sisiB_trapesium_entry = ttk.Entry(frame_trapesium)
sisiB_trapesium_entry.pack()
trapesium_label = ttk.Label(frame_trapesium, text="Masukkan sisi C :")
trapesium_label.pack(pady=10)
sisiC_trapesium_entry = ttk.Entry(frame_trapesium)
sisiC_trapesium_entry.pack()
trapesium_label = ttk.Label(frame_trapesium, text="Masukkan sisi D :")
trapesium_label.pack(pady=10)
sisiD_trapesium_entry = ttk.Entry(frame_trapesium)
sisiD_trapesium_entry.pack()
trapesium_label = ttk.Label(frame_trapesium, text="Masukkan tinggi :")
trapesium_label.pack(pady=10)
tinggi_trapesium_entry = ttk.Entry(frame_trapesium)
tinggi_trapesium_entry.pack()
hitung_trapesium_button = ttk.Button(frame_trapesium, text="Hitung", command=hitung_trapesium)
hitung_trapesium_button.pack(pady=10)
hasil_trapesium_label = ttk.Label(frame_trapesium, text="")
hasil_trapesium_label.pack()

# Lingkaran
lingkaran_label = ttk.Label(frame_lingkaran, text="Masukkan jari-jari:")
lingkaran_label.pack(pady=10)
jari_jari_lingkaran_entry = ttk.Entry(frame_lingkaran)
jari_jari_lingkaran_entry.pack()
hitung_lingkaran_button = ttk.Button(frame_lingkaran, text="Hitung", command=hitung_lingkaran)
hitung_lingkaran_button.pack(pady=10)
hasil_lingkaran_label = ttk.Label(frame_lingkaran, text="")
hasil_lingkaran_label.pack()

root.mainloop()