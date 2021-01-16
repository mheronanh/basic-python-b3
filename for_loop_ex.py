n = int(input("Masukkan jumlah customer: "))

nama = [0 for i in range(n)] #bisa dibiasakan untuk menggunakan .append sehingga tidak harus melakukan inisialisas yang berdampak pada penggunaan memori lebih efisien.
umur = [0 for i in range(n)]

for i in range(n):
    nama[i] = input("Masukkan nama customer ke-{}: ".format(i+1))
    umur[i] = int(input("Masukkan umur customer ke-{}: ".format(i+1)))

#printing the result
for i in range(n):
    print("Customer ke-{} bernama {} dengan umur {}".format(i+1, nama[i], umur[i]))



    