print("KONVERSI SUHU KELVIN")

#Entry
suhu = input("Masukkan suhu dalam Kelvin :")

#Rumus 
R = 4/5 * (float(suhu) - 273)
F = 9/5 * (float(suhu) - 273) + 32
C = (float(suhu) - 273)

#Output
print("Kelvin sama dengan :" + suhu)
print("Reamur :" + str(R))
print("Fahrenheit :" + str(F))
print("Celcius :" + str(C))