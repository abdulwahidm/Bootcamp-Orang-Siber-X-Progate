<<<<<<< HEAD

# Pertama-tama, mari kita lihat bagaimana function bekerja dalam Python. 
# Function adalah bagian dari code yang menjalankan tugas tertentu. 
print() # adalah salah satu contoh function, untuk mencetak teks 

# Seperti print, ada banyak function yang sudah tersedia 
# di Python yang dapat membuat coding lebih mudah. 
# Kita juga dapat membuat function Anda sendiri.

# Sintaksis untuk mendefinisikan function adalah sebagai berikut:
def greet():
    print('hello')

greet() #memanggil function greet yang sudah dibuat di atas
=======
# Pertama-tama, mari kita lihat bagaimana function bekerja dalam Python. 
# Function adalah bagian dari code yang menjalankan tugas tertentu. 
# print adalah salah satu contoh function, yang memudahkan Anda 
# untuk mencetak teks tanpa perlu untuk menulis banyak code.

# Function tidak akan dijalankan hanya dengan mendefinisikannya, 
# Anda perlu memanggil function untuk menjalankan code didalamnya. 
# Untuk memanggil sebuah function, Anda cukup menulis function_name(). 
# Perlu diingat bahwa function hanya dapat dipanggil setelah Anda mendefinisikannya.


# Untuk memberikan argument ke sebuah function, function harus mempunyai variable untuk menerimanya, 
# variable ini di sebut parameter. Pada contoh di bawah, 
# function greet memiliki parameter name untuk menerima sebuah argument.
'''
def print_hand(hand):
    print('Anda memilih: ' + hand)

print_hand('Batu')
print_hand('Kertas')
'''

# Kita juga bisa menambahkan lebih dari satu parameter ke dalam suatu function
# Tambahkan parameter ke print_hand
def print_hand(hand, name):
    # Ubah hasil ke '___ memilih: ___'
    print(name + ' memilih: ' + hand)

# Tambahkan argument ke dua ke print_hand
print_hand('Batu', 'Ninja Ken')

# Tambahkan argument ke dua ke print_hand
print_hand('Kertas', 'Komputer')

>>>>>>> 1bef5bb69940af18d16deb2265f1fea2b76e4979
