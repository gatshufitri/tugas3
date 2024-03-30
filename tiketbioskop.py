listfilm = {
   'Action': {1: {'Judul': 'Lift', 'Waktu': '15:00 - 17:00 WIT'},
               2: {'Judul': 'Star Wars', 'Waktu': '13:00 - 15:00 WIT'},
               3: {'Judul': 'Lupin', 'Waktu': '17:00 - 19:00 WIT'},
               4: {'Judul': 'Who is Erin', 'Waktu': '16:00 - 18:00 WIT'},
               5: {'Judul': 'Criminal code', 'Waktu': '14:00 - 16:00 WIT'}},
    'Horor': {1: {'Judul': 'Annabelle', 'Waktu': '17:00 - 19-00 WIT'},
              2: {'Judul': 'The Nun 1', 'Waktu': '16:00-18:00 WIT'},
              3: {'Judul': 'The Counjuring', 'Waktu': '15:00-16:00'},
              4: {'Judul': 'The Nun 2', 'Waktu': '15:30-16:53 WIT'},
              5: {'Judul': 'Valak', 'Waktu': '18:00-20:00 WIT'}},
    'Thrailer': {1: {'Judul': 'Bird Box', 'Waktu': '21:00-23:00 WIT'},
                 2: {'Judul': 'The Visit', 'Waktu': '15:00-17:00 WIT'},
                 3: {'Judul': 'The Medium', 'Waktu': '17:35-21:00 WIT'},
                 4: {'Judul': 'Gone Girl', 'Waktu': '16:00-18:00 WIT'},
                 5: {'Judul': 'Shutter Island', 'Waktu': '18:20-20:30 WIT'}}
}
listharga = {
    'Hari': {'Senin': '35.000',
             'Selasa': '35.000',
             'Rabu': '35.000',
             'Kamis': '35.000',
             'Jumat': '35.000',
             'Sabtu': '45.000',
             'Minggu': '50.000'}
}

print("Daftar Genre Film")
for genre in listfilm:
    print(genre)

pilih_genre = input("Pilih Genre Film: ")
if pilih_genre in listfilm:
    print(f"Daftar Film {pilih_genre}:")
    for nomor, film in listfilm[pilih_genre].items():
        print(f"{nomor}. {film['Judul']}")
    pilih_no_film = int(input("Silahkan Pilih Nomer Film : "))
    if pilih_no_film in listfilm[pilih_genre]:
        judul_film_dipilih = listfilm[pilih_genre][pilih_no_film]['Judul']
        waktu_film_dipilih = listfilm[pilih_genre][pilih_no_film]['Waktu']
    print(f"Waktu Film {judul_film_dipilih}: {waktu_film_dipilih}")


    print("Daftar Harga:")
    for hari, harga in listharga['Hari'].items():
        print(f"{hari}: Rp {harga}")

    pilih_hari = input("Pilih Hari: ")
    if pilih_hari in listharga['Hari']:
        print(f"Harga tiket untuk hari {pilih_hari}: Rp {listharga['Hari'][pilih_hari]}")
        while True :
            confrim = input("Apakah Anda Ingin Membeli Tiket ? [Y/T] : ")
            if confrim == 'Y' :
                jumlah_tiket = int(input("Masukan Jumlah Tiket : "))
                for tiket in range (jumlah_tiket):
                    masukan_nama = input("Masukan Nama Anda : ")
                    masukan_umur = int( input("Masukan Umur Anda : "))
                for x in range (jumlah_tiket):
                    if masukan_umur >=18 :
                        print("Anda Diperbolehkan Nonton")
                        print("Nama Anda  : ",masukan_nama)
                        print("Umur Anda  : ",masukan_umur)
                        print("Film       : ",judul_film_dipilih)
                        print("Waktu Film : ",pilih_hari)  
                        print("Quantity   : ",jumlah_tiket)
                    else :
                        print("Anda Tidak Diperbolehkan Nonton")    
            break
                       
    else:
        print("Hari tidak valid.")
else:
    print("Pilihan Tidak Valid")