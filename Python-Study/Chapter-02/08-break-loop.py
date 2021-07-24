# Kita dapat menggunakan statement break untuk keluar dari loop. 
# Statement break biasanya digabung dengan statement if, 
# seperti pada contoh di bawah. Ini dapat digunakan seperti pada loop while.

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)
    if number == 3:
        break # saat number sama dengan 3 maka loop akan terhenti
              # pada console yang tercetak 1 2 3

numbers = [765, 921, 777, 256]
for number in numbers:
    print(number)
    # ketika variable number adalah 777, cetak '777 ditemukan, hentikan loop' dan keluar dari loop
    if number == 777:
        print('777 ditemukan, hentikan loop')
        break
    
