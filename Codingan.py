"""
Nama = Muhammad Khairu Fadilah
NIM  = 2309116025
Tugas Posttest "Menghitung Rumus Segitiga Pythagoras"

"""
import math

def program():
    print(45*"=")
    print("Program Penghitung Rumus Segitiga Pythagoras")
    print(45*"=" + "\n")
    tanya = input("Anda ingin mecari sisi apa? (alas, tegak, miring) = ")

    if tanya == "alas":
        miring_1 = int(input("Masukkan panjang sisi miring = "))
        tegak_1 = int(input("Masukkan sisi tegak = "))
        alas_1_kua = (miring_1**2) - (tegak_1**2)
        alas_1 = math.sqrt(alas_1_kua)
        print(f"Sisi alas dari segitiga ini adalah {alas_1}.")
    elif tanya == "tegak":
        miring_2 = int(input("Masukkan panjang sisi miring = "))
        alas_2 = int(input("Masukkan sisi alas = "))
        tegak_2_kua = (miring_2**2) - (alas_2**2)
        tegak_2 = math.sqrt(tegak_2_kua)
        print(f"Sisi tegak dari segitiga ini adalah {tegak_2}.")
    elif tanya == "miring":
        alas_3 = int(input("Masukkan panjang sisi alas = "))
        tegak_3 = int(input("Masukkan sisi tegak = "))
        miring_3_kua = (alas_3**2) + (tegak_3**2)
        miring_3 = math.sqrt(miring_3_kua)
        print(f"Sisi miring dari segitiga ini adalah {miring_3}.")
    else:
        print("Input error!")

print(45*"=")
print("Sebelum Memasuki Program, Silahkan Login Terlebuh Dahulu")
print(45*"=")
user = input("Username: ")
sandi = input("NIM: ")

if sandi == "2309116025" and user == "Muhammad Khairu Fadilah":
    print("Selamat datang KHAIRU"+"\n")
    program()
    
else:
    print("Username atau NIM salah, mohon mencoba lagi")
