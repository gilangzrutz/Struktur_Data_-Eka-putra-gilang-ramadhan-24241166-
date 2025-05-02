def hitung_luas():
    pilihan = input("Hitung luas (1: Persegi Panjang, 2: Segitiga): ")
    if pilihan == "1":
        panjang, lebar = float(input("Panjang: ")), float(input("Lebar: "))
        print(f"Luas: {panjang * lebar}")
    elif pilihan == "2":
        alas, tinggi = float(input("Alas: ")), float(input("Tinggi: "))
        print(f"Luas: {0.5 * alas * tinggi}")
    else:
        print("Pilihan tidak valid.")

hitung_luas()