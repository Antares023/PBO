import random 

#membuat angka random untuk kode verifikasi
angka_random = random.randint(1000, 9999)

print(angka_random)

ulang = input("Apakah anda ingin mengganti kode verifikasi 4 digit (yes/no)?")
if ulang == "yes":
    print(angka_random)
else :
    print("TERIMA KASIH!!!")