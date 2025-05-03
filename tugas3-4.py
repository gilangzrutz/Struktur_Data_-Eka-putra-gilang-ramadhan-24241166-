# Program menghitung luas persegi panjang atau segitiga
print("Apakah Anda ingin menghitung luas persegi panjang atau segitiga?")
print("1. Persegi Panjang")
print("2. Segitiga")

# Input pilihan pengguna
pilihan = input("Masukkan pilihan (1/2): ")

if pilihan == "1":
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    luas = panjang * lebar
    print(f"Luas persegi panjang adalah {luas}")
elif pilihan == "2":
    alas = float(input("Masukkan alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    luas = 0.5 * alas * tinggi
    print(f"Luas segitiga adalah {luas}")
else:
    print("Pilihan tidak valid. Silakan coba lagi.")
