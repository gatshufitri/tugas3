kel4 = '''
=============== Tiket Bioskop ==============
============== Keloompok Empat =============
'''
print(kel4)

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
listkel4 = {
    'Nama':{'Muhamad Gatshu Fitri': '07352311183',
            'M Thaariq Ramadhan': '07352211165',
            'Mujaddid Muslim Mubarak Patty': '07352311161',
            'Nabila Azahra Assagaf': '07352311163',
            'Ningketaty Aryani Uropmabin': '07352211111',
            'Serli Muhammad': '07352311175',
            'Yusri Malagapi': '07352111021',
            'Nurlini Ibrahim': '02352111016',
            'Wahdania Afendi': '07352311177',
            'Nabil Tamim Abdullah': '07352311162'}
}
listnama = []
listumur = []
listduduk = []
listbaris = []
listkolom = []

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
        waktu_film_dipilih = listfilm[pilih_genre][pilih_no_film]['Waktu']
        print(f"Waktu Film {judul_film_dipilih}: {waktu_film_dipilih}")    

    print('''\n======== Silahkan Pilih Hari =========
======= Untuk Menentukan Harga =======''')
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
                   
            def peta_bioskop (baris,kolom):
                for duduk in range  (baris):
                    listduduk.append(['0']*kolom)
                return listduduk
            def tampilkan_peta(listduduk):
                for baris in listduduk:
                    print(' '.join(baris))
            def pilih_tempat_duduk(listduduk):
                for tempat in range (jumlah_tiket):
                    masukan_baris = int(input(f"Masukan Nomer Baris Orang Ke-{tempat+1}: "))
                    masukan_kolom = int(input(f"Masukan Nomer Kolom orang Ke-{tempat+1}: "))
                    listbaris.append (masukan_baris)
                    listkolom.append (masukan_kolom)
                    if listduduk[masukan_baris - 1][masukan_kolom - 1] == 'X':
                        print("Tempat Duduk Tersebut Sudah Teerisi.")
                    else :
                        listduduk[masukan_baris - 1][masukan_kolom - 1] = 'X'
                        print("Tempat Duduk Berhasil Dipilih")
            break        
        buat_peta_bioskop = peta_bioskop(5,5)
    
        print("\n==== Peta Tempat Duduk Bioskop ====")
        tampilkan_peta(buat_peta_bioskop)
        pilih_tempat_duduk(buat_peta_bioskop)
        print("\nPeta Tempat Duduk Bioskop Setelah Dipilih : ")
        tampilkan_peta(buat_peta_bioskop)   
               
        
        import sys
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
                    import sys
                    print("1. Exit")
                    masukan_pilihan = input("Pilih Menu (1) : ")
                    if masukan_pilihan == "1":
                        print("Terimakasih Sudah Berkunjung")
                        sys.exit()
                    else:
                        print("Pilihan Tidak Valid")
                            
            elif masukan_pilihan == "2":
                for info in range (jumlah_tiket):
                         print("\n============== Informasi Tiket ==============")
                         print("Nama Anda    : ",listnama[info])
                         print("Umur Anda    : ",listumur[info])
                         print("Film         : ",judul_film_dipilih)
                         print("Waktu Film   : ",pilih_hari,waktu_film_dipilih)
                         print("Jumlah Tiket : ",jumlah_tiket)
                         print("Tempat Duduk : ","Baris",listbaris[info],"Kolom",listkolom[info])
                         tampilkan_peta(buat_peta_bioskop)
                         print("Terimakasih",listnama[info],"Telah Memesan Tiket",judul_film_dipilih)
                         print("=============================================")
                while True :
                    import sys
                    print("1. Exit")
                    masukan_pilihan = input("Pilih Menu (1) : ") 
                    if masukan_pilihan == "1":
                        print("Terimakasih Sudah Berkunjung")
                        sys.exit()
                    else :
                         print("Pilihan Tidak Valid")                            
                
            elif masukan_pilihan == "3":
                 print("Terimakasih Sudah Berkunjung")
                 sys.exit()
            else :
                print("Pilihan Tidak Valid")                               
    else:
        print("Hari tidak valid Silahkan Refresh.")
else:
    print("Pilihan Tidak Valid Silahkan Refresh")