print(10 < 6)
print(10 > 6)
print(1 == 1)

a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))

#branching
if (a > b):
    print("{} lebih besar dari {}".format(a, b))
elif (a == b):
    print("{} sama dengan {}".format(a, b))
else:
    print("{} lebih kecil dari {}".format(a,b))

#contoh kedua : bilangan prima (kasus untuk integer > 2)
x = int(input("Periksa bilangan berikut: "))
prime = False
for i in range(2, x):
    if (x % i == 0):
        print("{} bukan bilangan prima".format(x))
        prime = False
        break
    else:
        prime = True
if prime == True:
    print("{} adalah bilangan prima".format(x))
