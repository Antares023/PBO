print("Konversi Suhu Kelvin")
def get_reamur(suhu):
    R = 4/5 * (float(suhu) - 273)
    return R

def get_fahrenheit(suhu):
    F = 9/5 * (float(suhu) - 273) + 32
    return F
    
def get_celcius(suhu):
    C = (float(suhu) - 273)
    return C

#Entry
suhu = input("Masukkan suhu dalam Kelvin :")

#Rumus
R = get_reamur(suhu)
F = get_fahrenheit(suhu)
C = get_celcius(suhu)

#Output
print("Kelvin sama dengan :" + suhu)
print("Reamur :" + str(R))
print("Fahrenheit :" + str(F))
print("Celcius :" + str(C))