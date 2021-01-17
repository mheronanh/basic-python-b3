import os
from time import sleep

#inisiasi global variable
kontak = {
    'nama' : [],
    'telepon' : []
}

#pesan selamat datang
def welcome(): 
    print("Selamat datang!")
    sleep(1)
    os.system('cls')

#fungsi untuk menampilkan menu
def menu():
    print("--Menu--")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    option = int(input("Pilih menu: "))
    os.system('cls')
    return option

#prosedur untuk menampilkan daftar kontak yang sudah ada
def daftar_kontak():
    global kontak
    print("Daftar kontak:")
    if len(kontak['nama']) < 1:
        print("Data masih kosong!")
    else:
        for i in range(len(kontak['nama'])):
            print('Nama: ' + kontak['nama'][i])
            print('No Telepon: ' + kontak['telepon'][i])
    sleep(2)
    #atasi kasus jika data banyak dan waktu untuk melihat lebih panjang
    input("Silahkan enter untuk melanjutkan...")
    os.system('cls')

#prosedur untuk melakukan penambahan kontak
def tambah_kontak():
    global kontak
    kontak['nama'].append(input("Nama: "))
    kontak['telepon'].append(input("No Telepon: "))
    os.system('cls')
    print("Kontak berhasil ditambahkan")
    sleep(1)
    os.system('cls')

#prosedur untuk menampilkan pesan keluar
def keluar():
    print("Program selesai, sampai jumpa!")

#prosedur untuk menampilkan pesan opsi menu tidak diketahui
def unknown():
    print("Menu tidak tersedia")
    sleep(1)
    os.system('cls')

#prosedur program secara keseluruhan
def main():
    welcome()
    while True:
        opsi = menu()
        if opsi == 1:
            daftar_kontak()
        elif opsi == 2:
            tambah_kontak()
        elif opsi == 3:
            keluar()
            break
        else:
            unknown()

#testing
main()





