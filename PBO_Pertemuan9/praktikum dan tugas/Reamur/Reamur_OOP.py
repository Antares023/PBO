class reamur:
    def __init__(self, suhu):
        self.suhu = suhu

    def get_reamur(self):
        val = self.suhu
        return val
    
    def get_celcius(self):
        val = 5/4 * (self.suhu)
        return val

    def get_fahrenheit(self):
        val = (9/4 * self.suhu) + 32
        return val
    
    def get_kelvin(self):
        val = 5/4 * (self.suhu) + 273
        return val
    
suhu = input("Masukkan suhu dalam Kelvin :")
R = reamur(float(suhu))
val = R.get_reamur()

C = R.get_celcius()
F = R.get_fahrenheit()
K = R.get_kelvin()

#Output
print("Kelvin sama dengan :" + str(val))
print("Reamur :" + str(R))
print("Fahrenheit :" + str(F))
print("Celcius :" + str(C))