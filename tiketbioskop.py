listfilm = {
   'Action': {1: {'Judul': 'Lift', 'Waktu': '15:00 - 17:00 WIT'},
               2: {'Judul': 'Star Wars', 'Waktu': '13:00 - 15:00 WIT'},
               3: {'Judul': 'Lupin', 'Waktu': '17:00 - 19:00 WIT'},
               4: {'Judul': 'Who is Erin', 'Waktu': '16:00 - 18:00 WIT'},
               5: {'Judul': 'Criminal code', 'Waktu': '14:00 - 16:00 WIT'}},
    'Horror': {1: {'Judul': 'Annabelle', 'Waktu': '17:00 - 19-00 WIT'},
              2: {'Judul': 'The Nun 1', 'Waktu': '16:00-18:00 WIT'},
              3: {'Judul': 'The Counjuring', 'Waktu': '15:00-16:00'},
              4: {'Judul': 'The Nun 2', 'Waktu': '15:30-16:53 WIT'},
              5: {'Judul': 'Valak', 'Waktu': '18:00-20:00 WIT'}},
    'Thriller': {1: {'Judul': 'Bird Box', 'Waktu': '21:00-23:00 WIT'},
                 2: {'Judul': 'The Visit', 'Waktu': '15:00-17:00 WIT'},
                 3: {'Judul': 'The Medium', 'Waktu': '17:35-21:00 WIT'},
                 4: {'Judul': 'Gone Girl', 'Waktu': '16:00-18:00 WIT'},
                 5: {'Judul': 'Shutter Island', 'Waktu': '18:20-20:30 WIT'}},
    'Science Fiction': {1: {'Judul': 'Tenet', 'Waktu': '21:00-23:00 WIT'},
                 2: {'Judul': 'Interstellar', 'Waktu': '15:00-17:00 WIT'},
                 3: {'Judul': 'Oppenheimer', 'Waktu': '17:35-21:00 WIT'},
                 4: {'Judul': 'The Martian', 'Waktu': '16:00-18:00 WIT'},
                 5: {'Judul': 'Inception', 'Waktu': '18:20-20:30 WIT'}}
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
listnama = []
listumur = []

print("====Daftar Genre Film====")
for genre in listfilm:
    print(genre)

pilih_genre = input("Pilih Genre Film : ")
if pilih_genre in listfilm:
    print(f"\n====Daftar Film {pilih_genre}====")
    for nomor, film in listfilm[pilih_genre].items():
        print(f"{nomor}. {film['Judul']}")

    pilih_no_film = int(input("Silahkan Pilih Nomer Film (1-5) : "))
    if pilih_no_film in listfilm[pilih_genre]:
        judul_film_dipilih = listfilm[pilih_genre][pilih_no_film]['Judul']
        waktu_film_dipilih = listfilm[pilih_genre][pilih_no_film]['Waktu']
    print(f"Waktu Film {judul_film_dipilih}: {waktu_film_dipilih}")


    print("\n====Silahkan Pilih Hari=====")
    for hari, harga in listharga['Hari'].items():
        print(f"{hari}")

    pilih_hari = input("Pilih Hari : ")
    if pilih_hari in listharga['Hari']:
        print(f"Harga tiket untuk hari {pilih_hari}: Rp {listharga['Hari'][pilih_hari]}")
        while True :
            confrim = input("\nApakah Anda Ingin Membeli Tiket ? [Y/T] : ")
            if confrim == 'Y' :
                jumlah_tiket = int(input("Masukan Jumlah Tiket : "))
            
                for tiket in range (jumlah_tiket):
                    masukan_nama = (input(f"Masukan Nama Orang Ke -{tiket+1}: "))
                    masukan_umur = int(input("Masukan Umur Anda : "))
                    listnama.append (masukan_nama)
                    listumur.append (masukan_umur)

                for x in range (masukan_umur):
                    if masukan_umur >=18 :
                        print("Anda Diperbolehkan Nonton")                        
                    else :
                        print("Anda Tidak Diperbolehkan Nonton")
                    break  
                for info in range (jumlah_tiket):
                    print("\n====Informasi Tiket====")
                    print("Nama Anda    : ",listnama[info])
                    print("Umur Anda    : ",listumur[info])
                    print("Film         : ",judul_film_dipilih)
                    print("Waktu Film   : ",pilih_hari,waktu_film_dipilih)
                    print("Jumlah Tiket : ",jumlah_tiket)
                    print("Terimakasih",listnama[info],"Telah Memesan Tiket",judul_film_dipilih)
            break
                       
    else:
        print("Hari tidak valid.")
else:
    print("Pilihan Tidak Valid")