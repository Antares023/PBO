print(40* "=")
print("SELAMAT DATANG DI KALKULATOR SEDERHANA")
print(40* "=")

# Pilihan Operator
print("1. Penjumlahan \n", "2. Pengurangan \n", "3. Perkalian \n", "4. Pembagian \n", "5. Pangkat \n")
pilihan = input("Masukkan pilihan operator :")

# Rumus Operator
if pilihan == "1":
    angka1 = float(input("Masukkan angka pertama :"))
    angka2 = float(input("Masukkan angka kedua :"))
    hasil = angka1 + angka2
    print("Hasilnya adalah :", hasil)
elif pilihan == "2":
    angka1 = float(input("Masukkan angka pertama :"))
    angka2 = float(input("Masukkan angka kedua :"))
    hasil = angka1 - angka2
    print("Hasilnya adalah :", hasil)
elif pilihan == "3":
    angka1 = float(input("Masukkan angka pertama :"))
    angka2 = float(input("Masukkan angka kedua :"))
    hasil = angka1 * angka2
    print("Hasilnya adalah :", hasil)
elif pilihan == "4":
    angka1 = float(input("Masukkan angka pertama :"))
    angka2 = float(input("Masukkan angka kedua :"))
    hasil = angka1 / angka2
    print("Hasilnya adalah :", hasil)
elif pilihan == "5":
    angka = float(input("Masukkan angka :"))
    hasil = angka ** 2
    print("Hasilnya adalah :", hasil)

print("TERIMA KASIH TELAH MENJALANKAN PROGRAM")