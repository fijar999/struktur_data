#aray append py (menambahkan element ke array)
import array as arr
a = arr.array('i', [1,2,3]) #array dengan tipe integer
print('array integer sebelum dilakukan insert: ', end=' ')
for i in range (0,3):
    print(i, end=' ')
print()

#menambahkan elemen dengan fungsi insert
a.insert(1,4)
print('array integer setelah dilakukan insert: ', end=' ')
for i in (a):
    print(i, end=' ')
print()

#array dengan tipe float
b=arr.array('d', [2.5, 3.2, 3.3])
print('array float sebelum dilakukan insert: ', end=' ')
for i in range(0,3):
    print(b[i], end=' ')
print()

#menambahkan elemnt dengan append
b.append(4.4)
print('array float setelah dilakukan insert: ', end=' ')
for i in (b):
    print(i, end=' ')
print()