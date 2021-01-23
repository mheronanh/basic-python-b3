def menu():
    print("Menu: ")
    print("1. Lihat daftar kontak")
    print("2. Tambahkan kontak")
    print("3. Keluar")
    option = int(input("Masukkan pilihan: "))
    return option

def show():
    f = open("file_kontak.txt", "r")
    print("List nama kontak: ")
    print(f.read())
    f.close()

def add():
    f = open("file_kontak.txt", "a")
    nama = input("Masukkan nama: ")
    telepon = input("Masukkan nomor telepon: ")
    f.write(nama + "," + telepon)
    f.write("\n")
    f.close()

def unknown():
    print("Menu tidak tersedia")

def keluar():
    print("Terima kasih!")

while True:
    opsi = menu()
    if opsi == 1:
        show()
    elif opsi == 2:
        add()
    elif opsi == 3:
        keluar()
        break
    else:
        unknown()

        
    