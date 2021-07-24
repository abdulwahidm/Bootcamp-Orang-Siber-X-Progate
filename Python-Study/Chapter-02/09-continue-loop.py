# Tidak seperti statement break yang akan mengakhiri loop, 
# statement continue melewatkan loop untuk iterasi tertentu. 
# Statement continue dapat digunakan dengan cara yang sama pada loop for dan loop while.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    # Lewatkan loop untuk angka yang dapat di bagi 3
    if number % 3 == 0:
        continue
    print(number) #pada console yang angka 3, 6, 9 tidak tercetak