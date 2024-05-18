bilangan1 = int(input("Masukan Bilangan Pertama : "))
bilangan2 = int(input("Masukan Bilangan Kedua : "))

operatot_tambah = bilangan1+bilangan2
operator_unary_tambah = +bilangan1 
operator_kurang = bilangan1-bilangan2
operator_unary_kurang = -bilangan1
operator_perkalian = bilangan1*bilangan2
operator_pembagian = bilangan1/bilangan2
operator_modulo = bilangan1%bilangan2
operator_pangkat = bilangan1**bilangan2

print(bilangan1,"+",bilangan2,"=",operatot_tambah)
print("+",bilangan1,"=",operator_unary_tambah)
print(bilangan1,"-",bilangan2,"=",operator_kurang)
print("-",bilangan1,"=",operator_unary_kurang)
print(bilangan1,"*",bilangan2,"=",operator_perkalian)
print(bilangan1,":",bilangan2,"=",operator_pembagian)
print(bilangan1,"%",bilangan2,"=",operator_modulo)
print(bilangan1,"**",bilangan2,"=",operator_pangkat)