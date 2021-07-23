#Kondisi if adalah kondisi yang akan dieksekusi oleh program jika bernilai benar atau TRUE

nilai = 9

#jika kondisi benar/TRUE maka program akan mengeksekusi perintah dibawahnya

if(nilai > 7):
    print("Sembilan Lebih Besar Dari Angka Tujuh") # Kondisi Benar, Dieksekusi
#jika kondisi salah/FALSE maka program tidak akan mengeksekusi perintah dibawahnya
if(nilai > 10):
    print("Sembilan Lebih Besar Dari Angka Sepuluh") # Kondisi Salah, Maka tidak tereksekusi


#contoh tambahan
x = 10
# Jika x lebih besar dari 30, cetak 'x lebih besar dari 30'
if x > 30:
    print('x lebih besar dari 30')


money = 5
apple_price = 2
# Jika money sama dengan atau lebih besar dari apple_price, cetak 'Anda dapat membeli apel'
if money >= apple_price:
    print('Anda dapat membeli apel')


#Kondisi if else adalah jika kondisi bernilai TRUE maka akan dieksekusi pada if, tetapi jika bernilai FALSE maka akan dieksekusi kode pada else

nilai = 3
#Jika pernyataan pada if bernilai TRUE maka if akan dieksekusi, tetapi jika FALSE kode pada else yang akan dieksekusi.
if(nilai > 7):
    print("Selamat Anda Lulus")
else:
    print("Maaf Anda Tidak Lulus") #kondisi pada blok else yang akan dieksekusi


hari_ini = "Minggu"

if(hari_ini == "Senin"):
    print("Saya akan kuliah")
elif(hari_ini == "Selasa"):
    print("Saya akan kuliah")
elif(hari_ini == "Rabu"):
    print("Saya akan kuliah")
elif(hari_ini == "Kamis"):
    print("Saya akan kuliah")
elif(hari_ini == "Jumat"):
    print("Saya akan kuliah")
elif(hari_ini == "Sabtu"):
    print("Saya akan kuliah")
elif(hari_ini == "Minggu"): 
    print("Saya akan libur") #kondisi akan masuk pada kondisi ini


