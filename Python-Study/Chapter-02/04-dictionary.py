'''
Seperti list, dictionary python digunakan untuk mengelola kelompok data. 
Perbedaannya adalah dictionary menggunakan kunci (key) daripada nomor index. 
Pada dictionary, sebuah kunci dipasangkan dengan sebuah nilai (value) untuk membentuk satu element. 
Hal ini juga dikenal sebagai pasangan kunci-nilai (key-value).
'''

fruits = {'apel' : 'merah', 'pisang' : 'kuning', 'kelapa': 'hijau'}
print(fruits) 
#pada console mungkin urutan element dictionari akan berbeda dari yang didefinisikan
#Ini dikarenakan, tidak seperti list, dictionary tidak memiliki index yang tetap

print('Apel berwarna ' + fruits['apel']) #apel berwarna merah