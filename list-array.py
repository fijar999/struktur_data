#list py
listangka = [3,6,9,12]
listhuruf = ['a','b','c','d']
listrandom = [3,'a',6,'true',12]

print(listangka)
print(listhuruf)
print(listrandom)

print(type(listangka))
print(type(listhuruf))
print(type(listrandom))


#array mode py (menggunakan array khusus)
import array as arr
array_1 = arr.array('i', [3,6,9,12]) #buat aray tipe integer
print(array_1)
print(type(array_1))


#array new py (membuat array baru)
import array as arr #importing "array" untuk array baru
a=arr.array('i',[1,2,3]) #membuat array dengan tipe integer (1)
print('array yang baru dibuat adalah: ', end=' ')
for i in range (0,3):
    print(a[i], end=' ')
print()
