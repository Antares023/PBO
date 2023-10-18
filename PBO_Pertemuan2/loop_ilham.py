# While Loop
print(20* "=")
print("While Loop")
print(20* "=")

count = 0
while (count < 10):
    print("Menyatakan :", count)
    count = count + 1

print("PROGRAM SELESAI DIJALANKAN \n")


# For Loop
print(20* "=")
print("For Loop")
print(20* "=")

data = ["100", "80", "60", "40", "20", "0"]
for output in data:
  print("Data yang dimunculkan :", output)
print("\n")


# Nested Loop
print(20* "=")
print("Nested Loop")
print(20* "=")

row = int(input("Masukkan row :"))

for i in range(row):
    for j in range(i):
        print("*", end=' ')
    print()