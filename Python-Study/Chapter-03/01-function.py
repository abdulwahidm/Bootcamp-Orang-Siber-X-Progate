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

def print_hand(hand):
    print('Anda memilih: ' + hand)

print_hand('Batu')
print_hand('Kertas')
