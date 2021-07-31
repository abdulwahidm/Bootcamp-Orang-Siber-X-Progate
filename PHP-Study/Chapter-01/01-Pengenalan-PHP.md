# A. Apa Itu PHP?

Dengan HTML, ada limitasi bagaimana kita mengontrol apa yang ditampilkan. Dengan menggunakan PHP, kita dapat mengubah teks yang ditampilkan tergantung audiens dan situasi.

# B . Bagaimana Menulis PHP Code

Code PHP dapat tertanam di dalam HTML. Dengan menggunakan tag PHP spesial ```<?php ... ?>,``` kita dapat menulis instruksi didalamnya. Code yang ditulis di dalam ```<?php ... ?>``` akan diubah menjadi HTML dan ditampilkan.

# C. Sintaksis PHP

Titik koma ; digunakan untuk memisahkan statement di PHP. Akan ada error jika sintaksis kita kurang titik koma, jadi mari berhati-hati! Selain itu, baris-baris yang dimulai dengan // disebut komentar dan tidak dijalankan. Komentar tidak akan mempengaruhi code kita, namun sangat berguna untuk mendokumentasikan dan membuat catatan.

```php
<?php
    // Baris ini adalah komentar
    echo 'Halo'; 
    echo 'Belajar PHP';
?>
```
Kita dapat menggunakan echo untuk mencetak karakter yang disebut string. Gunakan tkita kutip satu ' atau kutip dua " untuk mencetak mereka.

```php
<?php
    // Baris ini adalah komentar
    echo 'Hello World';  // Hasil: Hello World
?>
```

# D. Variable

Variable diibaratkan kotak untuk menyimpan data. Kita mendefinisikan variable dengan menambah simbol $ diawal. Semua tipe data dapat disimpan menggunakan sintaksis ```$variableName = nilai;```. Dalam pemrograman, ```= `` artinya untuk menentukan nilai di kanan pada apa yang terletak di sebelah kiri.  

```php
<?php 
    $name = 'John'; // menyimnpan John ke variable name

    echo $name; // Hasil John
?>
```

# E. Operator

## 1. Operator Penugasan (assignment)

Digunakan untuk menuliskan nilai pada suatu variabel. 
Operator penugasan yang paling umum digunakan adalah 
operator 'sama dengan' =. Operator ini digunakan untuk 
mengisi variabel yang ada di sebelah kiri dengan nilai 
yang ada di sebelah kanan. Misalnya $x = 2 berarti 
kita mengisi variabel $x dengan nilai 2. Atau $x = $y 
yang berarti kita mengisi variabel $x dengan nilai 
yang ada di dalam variabel $y.

```php
    $x = 20;
    $y = 2;
    echo "nilai x sebelum assignment: $x <br>";
    $x += $y;
    echo "nilai x setelah assignment: $x <br>";
```

## 2. Operator Aritmatika

Operator Aritmatika digunakan untuk melakukan operasi 
aritmatik terhadap nilai numerik, seperti penjumlahan, 
pengurangan, perkalian, pembagian, dan sebagainya.

```php
    $x = 20;
    $y = 3;
    $z = $x + $y;

    echo $z;
```

## 3. Operator Perbandingan


### 3.1 Operator sama dengan ( == )

```php 
$x == $y  // TRUE bila nilai $x sama dengan $y 
```


### 3.2 Operator identik ( === )

```php
$x === $y // TRUE bila nilai $x sama dengan $y, DAN tipe data keduanya sama
```


### 3.3 Operator tidak sama dengan ( !== ) atau ( <> )

```php
$x != $y // TRUE bila nilai $x tidak sama dengan $y
$x <> $y // TRUE bila nilai $x tidak sama dengan $y
```


### 3.4 Opearator tidak identik ( !=)(

```php
$x !== $y // TRUE bila nilai $x tidak sama dengan $y ATAU tipe data keduanya berbeda
```

### 3.5 Opearator lebih dari ( > )
```php
$x > $y // TRUE bila nilai $x lebih dari $y
```


### 3.6 Opearator kurang dari ( < )
```php
$x < $y	// TRUE bila nilai $x kurang dari $y
```


### 3.7 Opearator lebih dari atau sama dengan ( >= )

```php
$x >= $y // TRUE bila nilai $x lebih dari atau sama dengan  $y
```

### 3.8 Opearator kurang dari atau sama dengan ( <= )

```php
$x <= $y // TRUE bila nilai $x kurang dari atau sama dengan $y
```

Semua operator perbandingan digunakan untuk membandingkan dua buah nilai numerik atau string. Output dari operasi ini adalah nilai ``TRUE`` atau ``FALSE``.

## 4. Operator Logika

Operator logika digunakan untuk membandingkan dua pernyataan kondisi. 
Kondisi yang dimaksud adalah nilai variabel atau hasil perbandingan variabel
dalam tipe data boolean (TRUE dan FALSE). Operator logika yang tersedia
diantaranya and, or, xor dan not.

### 4.1 Operator AND ( and atau && )
```php
    $x and $y
    $x && $y	
    // TRUE hanya bila $x and $y keduanya bernilai TRUE
```

### 4.2 Operator OR ( or atau || ) 

```php
    $x or $y
    $x || $y	
    TRUE bila salahsatu atau keduanya dari $x atau $y bernilai TRUE
```

### 4.3 Operator XOR ( xor )
```php
$x xor $y	
// TRUE bila hanya salah satu saja (tidak keduanya) dari $x atau $y bernilai TRUE
```

### 4.4 Operator NOT ( ! )

```php
!$x	// TRUE bila variable $x bernilai FALSE
```


# F. Penggabungan String

## 1. Penggabungan string dengan operator dot (.)

```php
    $lesson = 'PHP';
    echo $lesson.'Pemula';
    // Ha3.sil: PHP Pemula

    $level = 'Pemula';
    echo $lesson.$level;
    // Hasil: PHP Pemula
```

## 2. Penggabungan string dengan substistusi variable

```php
    $name3. = 'Ninja Ken';
    echo "Halo {$name}"; 
    // Hasil: Halo, Ninja Ken

    echo 'Halo, {$name}';
    // Hasil: Halo, {$name}
    // {$name} tidak dicetak sebagai variable dari string
    // karena pada cara substitusi variable harus menggunakan double quote
```

# G. Percabangan

## 1. Statement if

Statement if memungkinkan kita untuk membuat percabangan kondisional. Jika kita meletakkan kondisi di dalam () setelah if, code diantara tkita kurung { } akan dijalankan hanya jika kondisi benar. Gambar di bawah menunjukkan bagaimana statement if ditulis.

```php 
    $x = 20;
    if($x > 10) {
        echo '$x lebih besar dari 10'; 
        // kode akan dijalankan
    }

    $y = 20;
    if($y > 30) {
        echo '$y lebih besar dari 30'; 
        // kode tidak akan dijalankan karena kondisi false
    }
```
## 2. Statement else & elseif
Kita dapat menambahkan code untuk ketika kondisi adalah false. Jika statement if yang cocok salah, code di else akan dijalankan.

```php 
    $x = 20;
    if($x == 30) { //false
        echo '$x adalah 30'; 
        // kode akan dijalankan
    } else {
        echo '$x bukan 30';
        // code ini akan dijalankan
    }

```

```php
    $nilai = 80;

    if($nilai < 25){
    echo "Nilai: D";
    } else if($nilai < 50){
    echo "Nilai: C";
    } else if($nilai < 80){
    echo "Nilai: B";
    } else {
    echo "Nilai: A";
    }

    // Hasil: Nilai A
```

## 3. Statement Switch

Statemen switch digunakan untuk menjalankan satu diantara banyak blok kode
berrdasarkan kecocokan nilai yang dievaluasi.

```php
   switch(variabel){
        case a:
            // blok kode A
            break;
        case b:
            // blok kode B
            break;
        ...
        default:
            // blok kode default
    } 
```
Pada statemen switch, nilai variabel akan dievaluasi kecocokannya untuk setiap
case. Bila ditemukan kecocokan pada salah satu case, maka blok kode 
pada case tersebut akan dijalankan. Umumnya blok kode pada setiap case diakhiri
dengan perintah break; agar program langsung keluar dari blok statemen switch dan
tidak perlu lagi mengecek sisa case di bawahnya. Apabila tidak ada case yang cocok dengan nilai variabel, maka blok kode pada bagian default yang akan dijalankan.

## 4. Statement Swith(2)

Kita sudah paham bahwa switch akan menjalankan blok kode yang casenya cocok
dengan nilai variabel yang dievaluasi. Lalu bagaimana bila kita ingin 
menjalankan blok kode yang sama untuk beberapa case berbeda?

```php 
    switch($binatang){
        case "ayam":
            echo "jumlah kaki 2";
            break;
        case "bebek":
            echo "jumlah kaki 2";
            break;
        case "burung":
            echo "jumlah kaki 2";
            break;
        case "sapi":
            echo "jumlah kaki 4";
            break;
        case "kambing":
            echo "jumlah kaki 4";
            break;
        default:
            echo "jenis binatang tidak terdaftar.";
    }
```

Akan tetapi switch memperbolehkan cara yang lebih sederhana 
agar kita tidak perlu mengulang baris kode yang sama.

```php
    switch($binatang){
        case "ayam":
        case "bebek":
        case "burung":
            echo "jumlah kaki 2";
            break;
        case "sapi":
        case "kambing":
            echo "jumlah kaki 4";
            break;
        default:
            echo "jenis binatang tidak terdaftar.";
    }
```

# H. Array

Kita dapat menyimpan beberapa nilai secara bersamaan menggunakan array, 
sedangkan variable hanya dapat menangani satu nilai seperti yang kita pelajari 
sebelumnya. Sebuah array dapat dibayangkan seperti kotak dengan partisi 
didalamnya; setiap ruang berisi data, dan nama untuk setiap ruang diberi nomor 
index (0, 1, 2…).

Sintaksis dasar untuk mendeklarasikan sebuah array adalah sebagai berikut: 

```php
$arrayName = array(nilai1, nilai2,…);
```
Nomor index ditetapkan untuk setiap element array dalam urutan dari 0 
hingga element terakhir. Untuk mengambil data dari sebuah array, kita dapat
menggunakan nomor index seperti: $arrayName[nomorIndex].

```php
    $colors = array('Merah', 'Biru', 'Kuning');

    echo $colors[0]; // Merah
    
    $colors[] = 'Putih';
    
    echo $colors[3]; // Putih
```
 
# I. Array Associative

Array associative memungkinkan kita untuk mengelola kumpulan data seperti array 
biasa. Perbedaannya adalah daripada menggunakan nomor index untuk mengelola
element individu, kita dapat menentukan nilai sebagai kunci. Kunci bisa berbentuk 
string. kita dapat memasangkan kunci dan nilainya dengan => sebagai berikut:

```php 
    $arrayName = array('namaKunci' => 'nilai1', ...);
```        

```php
    $scores = array('Matematika' => 70, 'Bahasa' => 90, 'Sains' => 80);
    
    $scores['Sains'] += 5;
    
    echo $scores['Sains'];
```

# J. Perulangan

Kita menggunakan loop untuk melakukan sesuatu berulang kali. Misalnya, 
kita ingin mencetak angka dari 1 hingga 100. Dengan menggunakan loop, 
kita dapat mengurangi code panjang dan berulang menjadi hanya beberapa baris 
seperti yang ditunjukkan pada contoh di bawah ini.

## 1. For 
```php
    for ($i = 51; $i <= 100; $i++) {
      echo $i;
      echo '<br>';
    }
    // Hasil: 12345
```

## 2. While 
Loop while memungkinkan kita untuk mengulang code seperti loop for. 
Ketika sebuah kondisi ditentukan, code dalam loop akan dijalankan berulang kali  selama nilainya adalah true. Berbeda dari loop for, code untuk yang menaikkan
variable, $i++;, harus ditulis dalam loop. Ini adalah perbedaan penting antara
loop while dan for.

```php
    $i = 1; // inisialisasi variable
    while($i <= 10) { // memeriksa kondisi
        echo $i; // kode perulangan yg dijalankan selama kondisi true
        $i++ // memperbarui nilai pada variable $i dengan increment 1
    }
```

## 3. Do While

Statemen do..while mirip seperti statemen while, yakni menjalankan blok kode
berulang-ulang selama kondisi yang dicek bernilai true.

```php
$x = 0;
do {
    // kode yang akan dijalankan berulang
    echo $j;
    $j++
} while (j < 5>);
```

## 4. Infinite Loop (Tak Terbatas)

Jika kita lupa memperbarui nilai variable yang digunakan untuk kondisi di akhir
loop while, ini akan menyebabkan loop infinite karena kondisinya akan selalu true. 
Loop infinite akan memberikan beban besar pada komputer, jadi pastikan ada kondisi false di titik tertentu sebelum menjalankannya.

```php 
    $i = 1;
    while($i <= 100) { 
        echo $i;
        // tidak ada proses pembaruan nilai $i
        // maka loop untuk mencetak nilai dari $i
        // akan dilakukan selamanya karena kondisi selalu bernilai true
    }

```
## 5. Foreach Loop

Perulangan dengan statemen foreach hanya berlaku pada variabel array, 
digunakan untuk mengulang membaca setiap elemen array.

```php

    foreach ($array as $value) {
        // kode yang akan dijalankan berulang
    }

    // cases:
    $kegemaran = array(
        'aktivitas' => 'Berenang', 
        'makanan' => 'Singkong Keju', 
        'minuman' => 'Jus Alpukat'
    );

    foreach ($kegemaran as $value) {
        echo "$value <br>";
    }
    // Hasil: 
    // Berenang
    // Singkong Keju
    // Jus Alpukat

```


## 5. Stament break dan continue pada perulangan

Statement break secara paksa akan mengakhiri loop dan digunakan dalam statement 
berulang seperti loop (for, while, foreach, dll). Statement break umumnya 
digunakan dalam kombinasi dengan statement conditional seperti statement if.

1. statement break;

```php
    for($i = 1; $i <= 10; $i++) {
        if ($i > 5) {
            break; // keluar dari looping ketika $i = 6
        }
        echo $i;
    }
    // Hasil: 123456
```

2. stetemnt continue

Ketika statement break mengeluarkan kita dari loop, statement continue hanya 
melewatkan iterasi saat ini tetapi tetap melanjutkan loop. Statement continue 
juga bisa digunakan dalam statement iteratif seperti for, while,foreach, dll.

```php
    for($i = 1; $i <= 10; $i++) {
        if ($i % 2 === 0) {
            continue;   // ketika $i adalah bilangan genap, 
                        // proses loop saat tersebut akan diloncati
        }
        echo $i;
    }
    // Hasil: 13579
```


K. Fungsi

Function adalah bagian code yang dirancang untuk menyelesaikan tugas tertentu dan 
mereturn hasil. Beberapa function umum dan berguna sudah tertanam di PHP; 
function ini disebut built-in function. Misalnya ``strlen`` mengembalikan jumlah
karakter dalam sebuah string. Di sini, nilai dalam tanda kurung ``()`` disebut argument.

kita juga dapat membuat function sendiri. Saat kita mengelompokkan code di satu tempat, kita dapat membuat perubahan ke semua tempat yang digunakan sekaligus dengan mengedit function yang memuatnya. Ini jauh lebih mudah dikelola daripada mengubah banyak baris code yang terpisah dan hampir identik. Mari pelajari lebih lanjut tentang cara mendefinisikan function di slide berikutnya.

Gunakan sintaksis: ``function functionName() {...}`` untuk membuat function. 

panggil fungsi tsb menggunakan tanda kurung: ``functionName()``.

```php
    // Definisikan function getCircleArea 
    function getCircleArea($radius) {
      return $radius * $radius * 3;
    }
    
    // Panggil function getCircleArea dan tetapkan nilai return ke variable $circleArea
    $circleArea = getCircleArea(5);
    
    // Cetak variable $circleArea
    echo $circleArea;
```
    


