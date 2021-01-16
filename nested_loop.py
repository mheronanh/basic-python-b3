matriks = [
    [1,2],
    [3,4]
]

for i in range(len(matriks)):
    for j in range(len(matriks[i])):
        print(matriks[i][j])

#contoh kasus perkalian matriks
for i in range (len(matriks)):
    sum = 0
    for j in range(len(matriks)):
        sum = sum + (matriks[i][j]*matriks[j][i])
    print(sum)