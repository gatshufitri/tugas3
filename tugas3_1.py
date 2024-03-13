data_mahasisswa = {'Gatshu': '12345','Aridho': '23456','Salwan': '34567','Ilham': '45678','Nabil': '56789'
                   ,'Rizal': '67890','Agung': '78901','Destito': '89012','Fauzan': '90123','Safril': '10123'}

welcome = '''
==========================================================================
================== Selamat Datang Di SIMAK UNKHAIR =======================
========================= Silahkan Login =================================
==========================================================================
'''

print (welcome)


username = input ("Masukan Username Anda : ")
password = input ("Masukan Password Anda : ")

if username in data_mahasisswa and data_mahasisswa[username] == password :
    print ("Anda Berhasil Login Ke SIMAK")
else :
    print ("Login Gagal. Username Atau Password Anda Salah")