# MATERI 1 VARIABEL
nama = "pryscila dinda"
umur = 100
pekerjaan = "Ai engineer"

# print(nama, umur, pekerjaan)
# print(umur + 1)

# MATERI 2 DATA TYPE
nama = "pryscila dinda"
umur = 100
tinggi = 200.4
is_student = True

# print("Nama saya ", nama)
# print("umur saya ", umur)
# print("Tinggi saya ", tinggi)
# print("apakah saya mahasiswa? ", is_student)

# print(type(umur))
# print(type(tinggi))
# print(type(is_student))

# MATERI 3 OPERATOR
# MATEMATIKA//

a = 10
b = 3

# print(a + b)  # tambah
# print(a - b)  # kurang
# print(a * b)  # kali
# print(a / b)  # bagi

# print(a % b)  # sisa pembagian (modulo)
# print(a**b)  # pangkat


# PERBANDINGAN
# BIASA DIGUNAKAN DI IF

# print(a > b)  # lebih besar
# print(a < b)  # lebih kecil
# print(a == b)  # sama dengan
# print(a != b)  # tidak sama dengan

# hasil dari perbandingan diatas :
# True
# False
# False
# True

# umur = 30
# print(umur + 1)
# print(umur + 5)
# print(umur * 2)
# print(umur > 18)
# print(umur == 30)


# MATERI 4 INPUT

# nama = input("Siapa Nama kamu? ")
# print("halo ", nama)

# hasilnya akan halo dinda atau sesaui dengan nama yang di input

# karena secara default input tipe datanya string.
# mengubah input menjadi angka dengan:
# umur = int(input("berapa umur kamu ? "))
# print(umur, "tahun")

# pekerjaan = input("pekerjaan kamu apa? ")
# print("pekerjaan saya ", pekerjaan)


# MATERI NO 5 IF/ELSE

# gabungan antara input dan if
# umur = int(input("berapa umur mu ?"))

# if umur >= 18:
#     print("kamu sudah dewasa")
# else:
#     print("kamu belum dewasa")

# elif
# digunakan untuk lebih dari 2 kondisi

# if umur >= 18:
#     print("dewasa")
# elif umur >= 13:
#     print("remaja")
# else:
#     print("anak-anak")


# MATERI NO 6 FOR (PERULANGAN)

# for i in range(1, 6):
# print(i)


# MATERI NO 7 for loop + if
# untuk setiap data cek apakah memenuhi kondisi tertentu

# mencari ganjil
# for i in range(1, 10):
#     if i % 2 == 1:
#         print(i)


# for i in range(1, 11):
#     if i > 5:
#         print(i)

# for i in range(1, 11):
#     if i % 2 == 0:
#         if i > 4:
#             print(i)

# atau lebih ringkasnya:

# for i in range(1, 11):
#     if i % 2 == 0 and i > 4:
#         print(i)


# MATERI NO 8 LIST

buah = ["apel", "mangga", "jeruk"]
# print(buah[2])

hewan = ["kucing", "anjing", "kelinci", "burung"]
# print(hewan[2])

# list + for (perulangan)
hewan = ["kucing", "anjing", "kelinci", "burung"]
# for item in hewan:
# print(item)

# list + for (perulangan) + if
# angka = [1, 2, 3, 4, 5, 6]
# for i in angka:
#     if i % 2 == 0:
#         print(i)

# mengubah data di list
hewan = ["kucing", "anjing", "kelinci", "burung"]
hewan[1] = "tikus"
# print(hewan)

# menambahkan 1 data dari belakang di list
hewan = ["kucing", "anjing"]
hewan.append("burung")
print(hewan)

# menambahkan 1 data dari belakang di list
buah = ["apel", "mangga", "jeruk"]
buah.remove("mangga")
print(buah)


# buah = ["pepaya", "semangka", "salak", "belimbing", "jajan"]

# # menambahkan data
# buah.append("duku")
# # mengurangi data
# buah.remove("pepaya")

# # print(buah)

# # untuk memanggil list supaya rapih kebawah dengan loop
# # for item in buah:
# #     print(item)

# # dictionary/object di js
# user = {"nama": "supti", "umur": "22", "alamat": "jakarta"}
# # print(user[nama])

# # function
# def halo(nama):
#     print("halo", nama)


# halo("susi")
