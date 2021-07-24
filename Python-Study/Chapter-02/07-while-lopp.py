# Kita juga dapat menggunakan loop while untuk mengulang code.
# Dengan loop while, code akan diulangi sampai kondisi tertentu, 
# seperti jika x <= 100 mengevaluasi False.


# Sintaksis untuk loop while adalah sebagai berikut:
# while <conditional expression>:
# Code pada loop while akan terus berulang selama kondisi True.


# Jika kita lupa untuk memperbarui nilai variable yang digunakan 
# pada kondisi di akhir loop while, loop infinite (loop tak terbatas) 
# dapat terjadi karena kondisi selalu mengevaluasi True.
# Loop Infinite memberikan beban yang besar pada komputer, 
# jadi pastikan kondisi akan mengevaluasi False pada titik tertentu.

x = 10

# Buat loop while yang diulang selama x lebih besar dari 0
while x > 0:
    # Cetak variable x  
    print(x)
    # Kurangi 1 dari variable x 
    x -= 1