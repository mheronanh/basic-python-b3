f = open("file.txt", "r")
a = (f.readline()).split(" ")

for i in a:
    print(i)