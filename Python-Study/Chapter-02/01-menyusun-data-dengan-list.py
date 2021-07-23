'''
Mari belajar bagaimana mengelola sekelompok data dengan satu variable. 
Ketika ada daftar nama-nama makanan, sebagai contoh, tidak efisien untuk menamainya dengan variable terpisah, 
seperti food1, food2, food3. Akan lebih baik untuk mempunyai variable foods untuk mengelola keseluruhan daftar tersebut.

Seperti integer dan string, kita dapat menentukan list ke dalam satu variable. 
Sesuai norma penamaan yang berlaku, nama variable bersifat plural, 
seperti foods, karena variable akan mengandung banyak element.
'''

foods = ['gulai', 'sushi', 'mie']
print(foods) #akan menampilkan ['gulai', 'sushi', 'mie']


'''
Setiap element list dinomori 0, 1, 2, ....
Ini disebut nomor indeks. Nomor indeks dimulai dari 0. 
Kita bisa mendapatkan element individual dengan menulis list[index].
'''

print('Saya suka ' + foods[2]) #megambil element dengan index 2 dari list foods
#pada console akan menampilkan `Saya suka mie`

## Contoh 2:
fruits = ['apel', 'pisang', 'jeruk']

print(fruits[0]) #jeruk
print('Saya suka ' + fruits[2])