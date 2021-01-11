# Nama      : Muhammad Heronan Hyanda
# Batch     : 3
# Kelas     : C
# Mentor    : Nafi Maula Hakim

# Inisialisasi
nilai_teori = float(input("Masukkan nilai ujian teori: "))
nilai_praktek = float(input("Masukkan nilai ujian praktek: "))
threshold = 70

# Hasil
if (nilai_teori >= threshold) and (nilai_praktek >= threshold):
    print("Selamat, anda lulus!")
else:
    if nilai_teori >= threshold:
        print("Anda harus mengulang ujian praktek.")
    elif nilai_praktek >= threshold:
        print("Anda harus mengulang ujian teori.")
    else:
        print("Anda harus mengulang ujian teori dan praktek.")