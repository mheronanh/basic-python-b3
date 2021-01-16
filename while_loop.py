masukan = int(input("Masukkan banyak perulangan yang diinginkan: "))

i = 0
while i < masukan:
    print("Hai, kamu {}".format(i))
    i += 1

#contoh kasus: validasi
username = input("Masukkan username dengan panjang tidak kurang dari 8 karakter: ")
while len(username) < 8:
    username  = input("Masukkan username kembali: ")

#upgrade kasus validasi
while True:
    username = input("Masukkan username dengan panjang tidak kurang dari 8 karakter: ")
    if len(username) > 8:
        break
    else:
        print("Maaf, username kamu masih kurang dari 8 karakter, silahkan masukkan kembali!")
        continue #continue itu digunakan untuk skip/force loop untuk cek awal sedangkan pass digunakan untuk execute nothing 
print("Berhasil, username kamu benar!")