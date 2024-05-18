x = float(input("Nilai Pertama :"))
y = float(input("Nilai Kedua :"))

def penjumlahan(x, y):
    return x + y
def pengurangan(x,y):
    return x - y
def perkalian(x,y):
    return x * y
def pembagian(x,y):
    return x / y
def modulus(x,y):
    return x % y

print("Pilih operasi matematika:")
print("1. Penjumlahan (+)")
print("2. Pengurangan (-)")
print("3. Perkalian (*)")
print("4. Pembagian (/)")
print("5. Modulus (%)")

pilihan = input("Masukkan pilihan Anda (1/2/3/4/5): ")
if pilihan == '1':
    hasil = penjumlahan(x, y)
    print("Hasil penjumlahan:", hasil)
elif pilihan == '2':
    hasil = pengurangan(x, y)
    print("Hasil pengurangan:", hasil)
elif pilihan == '3':
    hasil = perkalian(x, y)
    print("Hasil perkalian:", hasil)
elif pilihan == '4':
    hasil = pembagian(x, y)
    print("Hasil pembagian:", hasil)
elif pilihan == '5':
    hasil = modulus(x, y)
    print("Hasil modulus:", hasil)
else:
    print("Pilihan tidak valid.")