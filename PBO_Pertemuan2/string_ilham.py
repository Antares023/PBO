print(30*"=")
print("SELAMAT DATANG DI STRING.PY")
print(30*"=")

# Data yang tersimpan
sayur = ["kangkung", "bayam", "wortel", "tomat", "bawang"]
data = input("Masukkan makanan pilihan anda :")

# Operator
if data in sayur:
    print(f"Saya sedang memakan sayur {data}")
else :
    print(f"Tidak terdapat di dalam data! {data}")