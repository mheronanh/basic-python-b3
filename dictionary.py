student = {}
student['kelas7'] = ['thorin', 'jack']
student['kelas8'] = ['nisqy', 'selfmade']

for kelas in student:
    for siswa in student[kelas]:
        print(siswa, end= " ")
    print('')