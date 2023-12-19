print("KONVERSI SUHU FAHRENHEIT")

#Entry
suhu = input("Masukkan suhu dalam Farenheit :")

#Rumus 
C = 5/9 * (float(suhu) - 32)
R = 4/9 * (float(suhu) - 32)
K = 5/9 * (float(suhu) - 32) + 273

#Output
print("Farenheit sama dengan :" + suhu)
print("Celcius :" + str(C))
print("Reamur :" + str(R))
print("Kelvin :" + str(K))