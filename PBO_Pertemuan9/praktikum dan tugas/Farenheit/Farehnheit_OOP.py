class fahrenheit:
    def __init__(self, suhu):
        self.suhu = suhu

    def get_fahrenheit(self):
        val = self.suhu
        return val
    
    def get_celcius(self):
        val = (5/9 * self.suhu) - 32
        return val

    def get_reamur(self):
        val = (4/9 * self.suhu) - 32
        return val
    
    def get_kelvin(self):
        val = (5/9 * self.suhu) - 32 + 273
        return val
    
suhu = input("Masukkan suhu dalam Fahrenheit :")
F = fahrenheit(float(suhu))
val = F.get_fahrenheit()

C = F.get_celcius()
R = F.get_reamur()
K = F.get_kelvin()

#Output
print("Farenheit sama dengan :" + str(val))
print("Celcius :" + str(C))
print("Reamur :" + str(R))
print("Kelvin :" + str(K))