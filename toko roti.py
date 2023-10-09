import os
from prettytable import PrettyTable
os.system ("cls")

# membuat list daftar menu roti yang dijual
roti = [
    ["roti coklat", "5000", "10"],
    ["roti keju", "6000", "10"],
    ["roti abon", "8000", "10"],
    ["roti tawar","10000", "10"],
    ["roti srikaya","10000", "10"]
]

#tampilan jika login sebagai pembeli
def beli():
    print("=" * 32)
    print("         LISA'S BAKERY      ")
    print("      SELAMAT BERBELANJA      ")
    print("=" * 32)
    print()
    tampilkan_menu()
    while True:
        menu = str(input("pilih nama menu yang ingin dibeli: "))
        jumlah = int(input("jumlah yang ingin dibeli: "))

        for i in range(len(roti)):
            if roti[i][0] == menu:
                nama_menu = roti[i][0]
                harga_menu = int(roti[i][1])
                total = harga_menu * jumlah
                print ("=" * 32)
                print ("        STRUK BELANJAAN")
                print ("=" * 32)
                print (f"""
    pesanan : {nama_menu}
    jumlah  : {jumlah}
    total   : Rp {total}
                    """)
                print ("=" * 32)
                print("TERIMA KASIH TELAH BERBELANJA")
                print ("=" * 32)

        while True:
            pilihan = input("Apakah ingin membeli lagi? (y/t): ").lower()
            if pilihan == "t":
                return
            elif pilihan == "y":
                break
            else:
                print("pilihan tidak tersedia")


#tampilan jika login sebagai admin
def admin() :
        while True:
            print("=" * 32)
            print("             Menu admin")
            print("=" * 32)
            print("1. Tambah menu roti")
            print("2. Tampilkan menu roti")
            print("3. Update menu roti")
            print("4. Hapus menu roti")
            print("5. Keluar")
            pilihan = input("Masukkan pilihan (1/2/3/4/5) : ")

            if pilihan == "1":
                menambah()
            elif pilihan == "2":
                tampilkan_menu()
            elif pilihan == "3":
                mengubah()
            elif pilihan == "4":
                menghapus()
            elif pilihan == "5":
                break
            else:
                print("Pilihan tidak valid. Coba lagi.")

# function untuk menambahkan data ke tabel
def menambah() :
    nama_roti = input("Masukkan nama roti: ")
    harga = input("Masukkan harga roti: ")
    stok = input("Jumlah stok roti: ")
    tambahan = [nama_roti, harga, stok]
    roti.append(tambahan)
    tampilkan_menu()

# function untuk menampilkan tabel
def tampilkan_menu():
    table = PrettyTable()
    table.field_names = ["Nama roti", "Harga", "Stok"]
    for item in roti:
        table.add_row(item)
    print(table)

# function untuk mengubah tabel
def mengubah() :
    menu = str(input("Masukkan nama menu yang ingin diubah: "))
    for i in range(len(roti)):
        if roti[i][0] == menu:
            menu = input("Masukkan nama menu baru: ")
            harga = input("Masukkan harga menu baru: ")
            stok= input("Masukkan stok: ")
            roti[i][0] = menu
            roti[i][1] = harga
            roti[i][2] = stok
            print(f"data berhasil diubah menjadi {menu}")
            tampilkan_menu()
            break
    else:
        print(f"{menu} menu tidak ditemukan")

# function untuk menghapus tabel
def menghapus() :
    menu = str(input("Masukkan nama roti yang ingin dihapus: "))
    salah = False

    for i in range(len(roti)):
        if roti[i][0] == menu:
            del roti[i]
            salah = True
            break

    if salah:
        print(f"{menu} telah dihapus.")
        tampilkan_menu()
    else:
        print(f"{menu} tidak ditemukan.")

# dictionary untuk menyimpan username dan password
users = {
    "admin": "adm123",
    "pembeli": "beli123"
}

# function untuk login
def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in users and users[username] == password:
        if username == "admin":
            print("Selamat datang, Admin!")
            admin()
        else:
            print("Selamat datang, Pembeli!")
            beli()
    else:
        print("Login gagal. Coba lagi.")

# program utama
while True:
    print("Selamat datang di program login")
    print("Pilih peran Anda:")
    print("1. Admin")
    print("2. Pembeli")
    print("3. Keluar")
    pilihan = input("Masukkan pilihan (1/2/3): ")

    if pilihan == "1":
        login()
    elif pilihan == "2":
        login()
    elif pilihan == "3":
        print("Terima kasih! dan sampai jumpa :).")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")