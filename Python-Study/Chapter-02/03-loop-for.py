#Loop for untuk mencetak semua element pada list

foods = ['bubur', 'gulai', 'sate']

print('Saya suka ' + foods[0])
print('Saya suka ' + foods[1])
print('Saya suka ' + foods[2])

'''
Jika kita ingin mencetak semua element pada list, 
tidak efisien untuk mengulang code yang sama seperti contoh code di atas.
kita dapat menggunakan loop for untuk memudahkan kita mencetak semua element.
'''

#menggunakan loop for
fruits = ['pisang', 'jeruk', 'anggur']
for fruit in fruits:
    print('Saya suka ' + fruit)
    
#pada console code di atas akan menampilkan
'''
Saya suka pisang
Saya suka jeruk
Saya suka anggur
'''
