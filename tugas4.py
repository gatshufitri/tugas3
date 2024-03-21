masukan_bilangan = int ( input ("Masukan Bilangan : "))
masukan_pilihan_user = int (input('''1.Bilangan Oktal
2.Bilangan Heksadesimal
3.Bilangan Desimal
4.Bilangan Biner 
Silahkan Pilih : ''' ))

bil_oktal = oct(masukan_bilangan) [2:]
bil_hex = hex(masukan_bilangan) [2:]
bil_des = masukan_bilangan
bil_bin = "{:08b}".format(masukan_bilangan)


def masukan_pilihan (pilihan) :
    if pilihan == 1 :
        print("Bilangan Oktal Dari",masukan_bilangan,"Adalah",bil_oktal)
    elif pilihan == 2 :
        print("Bilangan Heksadesimal Dari",masukan_bilangan,"Adalah",bil_hex)
    elif pilihan == 3 :
        print("Bilangan Desimal Dari",masukan_bilangan,"Adalah",bil_des)
    elif pilihan == 4 :
        print("Bilangan Biner Dari",masukan_bilangan,"Adalah",bil_bin)
    else :
        print("Pilihan Tidak Sesuai")

masukan_pilihan(masukan_pilihan_user)
    