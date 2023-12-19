print("KONVERSI SUHU REAMUR")

#Entry
suhu = input("Masukkan suhu dalam Reamur :")

#Rumus 
C = 5/4 * (float(suhu))
F = (9/4 * float(suhu)) + 32
K = 5/4 * (float(suhu)) + 273

#Output
print("Reamur sama dengan :" + suhu)
print("Celcius :" + str(C))
print("Fahrenheit :" + str(F))
print("Kelvin :" + str(K))