#nomor 1
print(*range(1, 22, 2), sep=", ")


#nomor 2
list1 = ['Se', 'an', 'ber', 'menger', 'so', 'in']
list2 = ['lamat', 'da', 'hasil', 'jakan', 'al', 'i']
hasil = []
for i in range(len(list1)):
    hasil.append(list1[i] + list2[i])
print(hasil)

#nomor 3
Tuple1 = ("Hari ini saya sedang melaksanakan Ujian Daspro")
manipulation = "Saya telah mengerjakan dan menyelesaikan semua soal ujian"
print(manipulation)

#nomor 4
nilai1 = 3
nilai2 = 2

hasil1 = nilai1 << nilai2
hasil2 = nilai2 << nilai1
print("Hasil Left Shift 3 << 2:", hasil1)
print("Hasil Left Shift 2 << 3:", hasil2)

bin_hasil1 = bin(hasil1)
bin_hasil2 = bin(hasil2)
print("Biner dari hasil 3 << 2:", bin_hasil1)
print("Biner dari hasil 2 << 3:", bin_hasil2)

#nomor 5
bilangan = int(input("Masukkan bilangan yang ingin dikonversi :"))
konversi1 = bin(bilangan)[2:]
konversi2 = oct(bilangan)
konversi3 = hex(bilangan)

print("Bilangan Biner \t\t: ", konversi1.zfill(8))
print("Bilangan Octal \t\t: ", konversi2)
print("Bilangan Hexadecimal \t: ", konversi3)
print("Bilangan Decimal \t: ", bilangan)

#nomor 6
n = 5
for i in range(n):
  m = n - i

  for j in range(m):
    print("*", end="")
  print()

#nomor 7
def data(name, age, height, weight):
    print("Nama:", name)
    print("Usia:", age, "tahun")
    print("Tinggi Badan:", height, "cm")
    print("Berat Badan:", weight, "kg")
data("Mutia Mahmud", 18, 163, 56)

#nomor 8
Data = [10, 7, 20, 50, 49, 22, 44]

for nilai in Data:
    print(nilai, end=' , ')

#nomor 9
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

#nomor 10
def sorts(*args):
    sorted_args = sorted(args)
    for num in sorted_args:
        print(num)

sorts(10, 20, 30)
sorts(40, 50, 60)