#Operasi Aritmatika
a = 10
b = 3 

#Operasi tambah +
tambah = a + b
print (a,'+',b,'=',tambah)

#Operasi pengurangan -
kurang = a - b
print (a,'-',b,'=',kurang)

#Operasi perkalian *
kali = a * b
print (a,'x',b,'=',kali)

#Operasi pembagian /
bagi = a / b
print (a,':',b,'=',bagi)

#Operasi eksponen **
pangkat = a ** b
print (a,'**',b,'=',pangkat)

#Operasi modulus %
modulus = a % b
print (a,'%',b,'=',modulus)

#Operasi floor division //
floor = a // b
print (a,'//',b,'=',floor)

#prioritas operasi aritmatika / operational predience

#Urutan prioritas 
# 1. () Paling OP
# 2. Exponen/pangkat **
# 3. Perkalian,Pembagian,modulus,floor division * / % //
# 4. penjumlahan & pengurangan + -

x = 3
y = 4
z = 5

hasil = x ** y * z + y / x - x % y // z
print(x, '**' ,y, '*' ,z, '+' ,y, '/' ,x, '-' ,x, '%' ,y, '//' ,z,'=',hasil)

hasil = x ** x / (y + z)
print( x, '**' ,x, '/',(y + z),'=',hasil)