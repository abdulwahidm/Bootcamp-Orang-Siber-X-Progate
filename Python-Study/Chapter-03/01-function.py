# Pertama-tama, mari kita lihat bagaimana function bekerja dalam Python. 
# Function adalah bagian dari code yang menjalankan tugas tertentu. 
# print adalah salah satu contoh function, yang memudahkan Anda 
# untuk mencetak teks tanpa perlu untuk menulis banyak code.

# Function tidak akan dijalankan hanya dengan mendefinisikannya, 
# Anda perlu memanggil function untuk menjalankan code didalamnya. 
# Untuk memanggil sebuah function, Anda cukup menulis function_name(). 
# Perlu diingat bahwa function hanya dapat dipanggil setelah Anda mendefinisikannya.

# Definisikan function print_hand 
def print_hand():
    print('Anda memilih: Batu')

# Panggil function print_hand 
print_hand()


# Untuk memberikan argument ke sebuah function, function harus mempunyai variable untuk menerimanya, 
# variable ini di sebut parameter. Pada contoh di bawah, 
# function greet memiliki parameter name untuk menerima sebuah argument.

def greet(name):
    print('Halo ' + name)

greet("Abdul")