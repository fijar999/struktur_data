#copy array
motor = ['yamaha', 'honda','suzuki']
#copy to motor2
motor2 = motor.copy()
print(motor2)


#count array
mahasiswa = ['hary', 'john', 'jalu', 'john']
#count
jumlah = mahasiswa.count('john')
print(jumlah)


#extend array
siswa = ['juki', 'ahmad', 'roni']
siswabaru = ['maya', 'ari','aji']
siswa.extend(siswabaru)
print(siswa)


#index array elemnt
kota=['jakarta','bandung','surabaya','makasar']
#cek posisi element bandung
x=kota.index('bandung')
print(x)


#insert array spesific position
fruits=['apple', 'banana','chery']
#innsert alamat index ke 1
fruits.insert(1, 'orange')
print(fruits)


#reverse
angka=[1,2,3,4,5]
angka.reverse()
print(angka)


#sort array
cars=['ford','bmw','volvo']
angka=[1,6,7,3,2,5]
cars.sort()
angka.sort()
print(cars)
print(angka)