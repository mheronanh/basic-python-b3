lingkaran = {
    'luas' : 0,
    'keliling' : 0
}

def dimensi_lingkaran(r):
    global lingkaran
    lingkaran['luas'] = 22/7 * (r**2)
    lingkaran['keliling'] = 2*22/7*r
    return lingkaran

print(dimensi_lingkaran(float(input("Masukkan r: "))))
