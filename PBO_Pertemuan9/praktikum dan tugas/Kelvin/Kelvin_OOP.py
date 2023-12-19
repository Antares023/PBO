class kelvin:
    def __init__(self, suhu):
        self.suhu = suhu

    def get_kelvin(self):
        val = self.suhu
        return val
    
    def get_reamur(self):
        val = 4/5 * (self.suhu - 273)
        return val

    def get_fahrenheit(self):
        val = 9/5 * (self.suhu - 273) + 32
        return val
    
    def get_celcius(self):
        val = (self.suhu - 273)
        return val
    
suhu = input("Masukkan suhu dalam Kelvin :")
K = kelvin(float(suhu))
val = K.get_kelvin()

R = K.get_reamur()
F = K.get_fahrenheit()
C = K.get_celcius()

#Output
print("Kelvin sama dengan :" + str(val))
print("Reamur :" + str(R))
print("Fahrenheit :" + str(F))
print("Celcius :" + str(C))