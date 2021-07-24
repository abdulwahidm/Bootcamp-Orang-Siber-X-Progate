
# Dengan menggunakan apa yang sudah kita pelajari, 
# mari kita memperbarui aplikasi belanja yang sudah kita buat di Python 1.
# kita akan mencetak hasil menurut jumlah buah yang dimasukkan pada console.

# Buat dictionary dengan kunci dan nilai, dan tetapkan ke variable items 
items = {'apel': 2, 'pisang': 4, 'jeruk': 6}
# Buat loop for yang mengambil kunci dari items
for item_name in items:
    # Cetak '--------------------------------------------------'
    print('--------------------------------------------------')
    # Cetak 'Harga setiap ___ ___ dolar'
    print('Harga setiap ' + item_name + ' ' + str(items[item_name]) + ' dolar')