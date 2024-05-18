# Latihan 1
# Buatlah aplikasi menghirtung suhu ruangan dengan fungction, nilai suhu diteima melalui inputan user
def hitung_suhu_ruangan():
    suhu = float(input("Masukkan suhu ruangan dalam derajat Celsius: "))
    if suhu < 18:
        print("Suhu ruangan terlalu dingin.")
    elif suhu > 25:
        print("Suhu ruangan terlalu panas.")
    else:
        print("Suhu ruangan nyaman.")
        
hitung_suhu_ruangan()