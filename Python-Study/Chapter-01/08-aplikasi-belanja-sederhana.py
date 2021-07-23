# Berikan 2 ke variable apple_price 
apple_price = 2

# Terima jumlah apel dengan menggunakan input(), dan berikan hasilnya ke variable input_count 
input_count = input('Mau berapa apel?: ')

# Ubah variable input_count ke integer, dan berikan hasilnya ke variable count 
count = int(input_count)

# Berikan hasil dari apple_price * count ke variable total_price 
total_price = apple_price * count

# Dengan menggunakan variable count, cetak 'Anda akan membeli .. apel'
print('Anda akan membeli ' +  str(count) + ' apel')

# Dengan menggunakan variable total_price, cetak 'Harga total adalah .. dolar'
print('Harga total adalah ' + str(total_price) + ' dolar')