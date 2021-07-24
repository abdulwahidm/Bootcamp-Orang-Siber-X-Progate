#  Seperti list, Anda dapat menggunakan loop for untuk melakukan pengulangan 
#  pada dictionary dengan menulis for nama_variable in nama_dictionary:.
#  Kunci dari tiap element ditentukan ke variable sementara.
#  Dengan demikian, Anda bisa mendapatkan nilai yang sesuai dengan variable, seperti bisa dilihat pada gambar di bawah.


fruits = {'apel': 'apple', 'jeruk': 'orange', 'anggur': 'grape'}

# Dengan loop for, cetak '___ adalah ___ dalam bahasa Inggris'
for kunci_fruit in fruits:
    print(kunci_fruit + ' adalah ' + fruits[kunci_fruit] + ' dalam bahasa Inggris')

