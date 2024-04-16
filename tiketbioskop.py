kel4 = '''
=============== Tiket Bioskop ==============
============== Keloompok Empat =============
'''
print(kel4)

listfilm = {
   'Action': {1: {'Judul': 'Lift'}, 2: {'Judul': 'Star Wars'},3: {'Judul': 'Lupin'},4: {'Judul': 'Who is Erin'},5: {'Judul': 'Criminal code'}},
    'Horror': {1: {'Judul': 'Annabelle'},2: {'Judul': 'The Nun 1'},3: {'Judul': 'The Counjuring'},4: {'Judul': 'The Nun 2'},5: {'Judul': 'Valak'}},
    'Thriller': {1: {'Judul': 'Bird Box'},2: {'Judul': 'The Visit'},3: {'Judul': 'The Medium'},4: {'Judul': 'Gone Girl'},5: {'Judul': 'Shutter Island'}},
    'Science Fiction': {1: {'Judul': 'Tenet'},2: {'Judul': 'Interstellar'},3: {'Judul': 'Oppenheimer'},4: {'Judul': 'The Martian'},5: {'Judul': 'Inception'}}
}
listharga = {
    'Hari': {'Senin': '35.000','Selasa': '35.000','Rabu': '35.000','Kamis': '35.000','Jumat': '35.000','Sabtu': '45.000','Minggu': '50.000'}
}
listkel4 = {
    'Nama':{'Muhamad Gatshu Fitri': '07352311183','M Thaariq Ramadhan': '07352211165','Mujaddid Muslim Mubarak Patty': '07352311161','Nabila Azahra Assagaf': '07352311163','Ningketaty Aryani Uropmabin': '07352211111','Serli Muhammad': '07352311175','Yusri Malagapi': '07352111021','Nurlini Ibrahim': '02352111016','Wahdania Afendi': '07352311177','Nabil Tamim Abdullah': '07352311162'}
}
listnama = []
listumur = []
listduduk = []


print("====== Daftar Genre Film ======")
for genre in listfilm:
    print(genre)

pilih_genre = input("Pilih Genre Film : ")
if pilih_genre in listfilm:
    print(f"\n======= Daftar Film {pilih_genre} =======")
    for nomor, film in listfilm[pilih_genre].items():
        print(f"{nomor}. {film['Judul']}")
    pilih_no_film = int(input("Silahkan Pilih Nomer Film (1-5) : "))
    if pilih_no_film in listfilm[pilih_genre]:
        judul_film_dipilih = listfilm[pilih_genre][pilih_no_film]['Judul']
        print(f"Judul Film : {judul_film_dipilih}")
    else :
        print("Nomer Tidak Valid")

    print('''\n======== Silahkan Pilih Hari =========
======= Untuk Menentukan Harga =======''')
    for hari, harga in listharga['Hari'].items():
        print(f"{hari}")

    pilih_hari = input("Pilih Hari : ")
    if pilih_hari in listharga['Hari']:
        print(f"Harga tiket untuk hari {pilih_hari}: Rp {listharga['Hari'][pilih_hari]}")
    else:
        print("Hari Tidak Valid")
        exit()
    import datetime

    def tampilkan_jadwal(jadwal):
        print("Jadwal tayang film:")
        for index, waktu in enumerate(jadwal):
            print(f"{index + 1}. {waktu.strftime('%H:%M')}")

    jadwal_tayang = [
        datetime.time(10, 0),
        datetime.time(13, 0),
        datetime.time(16, 0),
        datetime.time(19, 0)
    ]
    print("Silakan pilih waktu tayang yang tersedia : ")
    tampilkan_jadwal(jadwal_tayang)
    while True:
        try:
            pilihan = int(input("Masukkan nomor waktu tayang (1-4): ")) - 1
        
            if 0 <= pilihan < len(jadwal_tayang):
                waktu_terpilih = jadwal_tayang[pilihan]
                waktu = waktu_terpilih.strftime("%H:%M")
                print("Anda telah memilih waktu tayang pada:", waktu)
                break
            else:
                print("Nomor waktu tayang tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Masukkan nomor waktu tayang yang valid.")

else:
    print("Pilihan Tidak Valid,Silahkan Refresh Kembali")
    exit()
while True :
    confrim = input("\nApakah Anda Ingin Membeli Tiket ? [Y/T] : ")
    if confrim == 'Y' :
        jumlah_tiket = int(input("Masukan Jumlah Tiket : "))
    else:
        print("Terimakasih Sudah Berkunjung")
        exit()                        
        
    for tiket in range (jumlah_tiket):
        masukan_nama = (input(f"Masukan Nama Orang Ke -{tiket+1}: "))
        masukan_umur = int(input("Masukan Umur Anda : "))
        listnama.append (masukan_nama)
        listumur.append (masukan_umur)
        
        if masukan_umur >=18 :
            print("Anda Diperbolehkan Nonton")                        
        else :
            print("Anda Tidak Diperbolehkan Nonton")
            exit()
    break        
   
           
while True :
    print("\n======== Menu ========")
    print("1. Lihat Nama Kelompok")
    print("2. Informasi Tiket")
    print("3. Exit")
    masukan_pilihan = input("Pilih Menu (1-3) : ")
    if masukan_pilihan == "1":
        print("\n============ Kelompok 4 ============")
        for nama,npm in listkel4 ['Nama'].items():
            print(f"Nama : {nama}")
            print(f"NPM  : {npm}")
            print("====================================")
            
        while True :
            print("1. Exit")
            masukan_pilihan = input("Pilih Menu (1) : ")
            if masukan_pilihan == "1":
                print("Terimakasih Sudah Berkunjung")
                exit()
            else:
                print("Pilihan Tidak Valid")
                    
    elif masukan_pilihan == "2":
        for info in range (jumlah_tiket):
                 print("\n============== Informasi Tiket ==============")
                 print("Nama Anda    : ",listnama[info])
                 print("Umur Anda    : ",listumur[info])
                 print("Film         : ",judul_film_dipilih)
                 print("Waktu Film   : ",pilih_hari,",", waktu,"WIT")
                 print("Jumlah Tiket : ",jumlah_tiket)
                 print("Terimakasih",listnama[info],"Telah Memesan Tiket",judul_film_dipilih)
                 print("=============================================")
        while True :
            print("1. Exit")
            masukan_pilihan = input("Pilih Menu (1) : ") 
            if masukan_pilihan == "1":
                print("Terimakasih Sudah Berkunjung")
                exit()
            else :
                 print("Pilihan Tidak Valid")                            
        
    elif masukan_pilihan == "3":
         print("Terimakasih Sudah Berkunjung")
         exit()
    else :
        print("Pilihan Tidak Valid")
