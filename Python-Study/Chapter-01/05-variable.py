''''
Variabel adalah lokasi memori yang dicadangkan untuk menyimpan nilai-nilai. 
Ini berarti bahwa ketika kita membuat sebuah variabel kita memesan beberapa ruang di memori. 
Variabel menyimpan data yang dilakukan selama program dieksekusi, 
yang nantinya isi dari variabel tersebut dapat diubah oleh operasi - 
operasi tertentu pada program yang menggunakan variabel.

Variabel dapat menyimpan berbagai macam tipe data. Di Python, variabel mempunyai sifat yang dinamis, 
artinya variabel Python tidak perlu didekralasikan tipe data tertentu dan 
variabel Python dapat diubah saat program dijalankan.

Penulisan variabel Python sendiri juga memiliki aturan tertentu, yaitu :

1. Karakter pertama harus berupa huruf atau garis bawah/underscore _
2 .Karakter selanjutnya dapat berupa huruf, garis bawah/underscore _ atau angka
3. Karakter pada nama variabel bersifat sensitif (case-sensitif). Artinya huruf kecil dan huruf besar dibedakan. Sebagai contoh, variabel namaDepan dan namadepan adalah variabel yang berbeda.
4. Untuk mulai membuat variabel di Python caranya sangat mudah, kita cukup menuliskan variabel lalu mengisinya dengan suatu nilai dengan cara menambahkan tkita sama dengan = diikuti dengan nilai yang ingin dimasukan.

Dibawah ini adalah contoh penggunaan variabel dalam bahasa pemrograman Python
'''

#proses memasukan data ke dalam variabel
nama = "Abdul Wahid"
#proses mencetak variabel
print(nama)

#nilai dan tipe data dalam variabel  dapat diubah
umur = 20           #nilai awal
print(umur)         #mencetak nilai umur
print(type(umur))   #mengecek tipe data umur

nama_depan= "Muryadi"
nama_belakang = "Saputra"
nama_lengkap = nama_depan + " " + nama_belakang
usia = 22
hobi = "Berenang"
print("Biodata: " , nama_lengkap, "usia: ", usia, "hobi: ", hobi)


panjang = 10
lebar = 5
luas = panjang * lebar
print(luas)

