# A. Apa Itu PHP?

Dengan HTML, ada limitasi bagaimana kita mengontrol apa yang ditampilkan. Dengan menggunakan PHP, Anda dapat mengubah teks yang ditampilkan tergantung audiens dan situasi.

# B . Bagaimana Menulis PHP Code

Code PHP dapat tertanam di dalam HTML. Dengan menggunakan tag PHP spesial ```<?php ... ?>,``` Anda dapat menulis instruksi didalamnya. Code yang ditulis di dalam ```<?php ... ?>``` akan diubah menjadi HTML dan ditampilkan.

# C. Sintaksis PHP

Titik koma ; digunakan untuk memisahkan statement di PHP. Akan ada error jika sintaksis Anda kurang titik koma, jadi mari berhati-hati! Selain itu, baris-baris yang dimulai dengan // disebut komentar dan tidak dijalankan. Komentar tidak akan mempengaruhi code Anda, namun sangat berguna untuk mendokumentasikan dan membuat catatan.

```php
<?php
    // Baris ini adalah komentar
    echo 'Halo'; 
    echo 'Belajar PHP';
?>
```
Kita dapat menggunakan echo untuk mencetak karakter yang disebut string. Gunakan tanda kutip satu ' atau kutip dua " untuk mencetak mereka.

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
    Digunakan untuk menuliskan nilai pada suatu variabel. Operator penugasan yang paling umum digunakan adalah operator 'sama dengan' =. Operator ini digunakan untuk mengisi variabel yang ada di sebelah kiri dengan nilai yang ada di sebelah kanan. Misalnya $x = 2 berarti kita mengisi variabel $x dengan nilai 2. Atau $x = $y yang berarti kita mengisi variabel $x dengan nilai yang ada di dalam variabel $y.

```php
    $x = 20;
    $y = 2;
    echo "nilai x sebelum assignment: $x <br>";
    $x += $y;
    echo "nilai x setelah assignment: $x <br>";
```

## 2. Operator Aritmatika
    Operator Aritmatika digunakan untuk melakukan operasi aritmatik terhadap nilai numerik, seperti penjumlahan, pengurangan, perkalian, pembagian, dan sebagainya.

```php
    $x = 20;
    $y = 3;
    $z = $x + $y;

    echo $z;
```

## 3. Operator Perbandingan


### 3.1 Operator sama dengan " == "

```php 
$x == $y  // TRUE bila nilai $x sama dengan $y 
```


### 3.2 Operator identik " === "

```php
$x === $y // TRUE bila nilai $x sama dengan $y, DAN tipe data keduanya sama
```


### 3.3 Operator tidak sama dengan " != " atau " <> "

```php
$x != $y // TRUE bila nilai $x tidak sama dengan $y
$x <> $y // TRUE bila nilai $x tidak sama dengan $y
```


### 3.4 Opearator tidak identik " !== "

```php
$x !== $y // TRUE bila nilai $x tidak sama dengan $y ATAU tipe data keduanya berbeda
```

### 3.5 Opearator lebih dari " > "

```php
$x > $y // TRUE bila nilai $x lebih dari $y
```


### 3.6 Opearator kurang dari " < "

```php
$x < $y	// TRUE bila nilai $x kurang dari $y
```


### 3.7 Opearator lebih dari atau sama dengan " >= "

```php
$x >= $y // TRUE bila nilai $x lebih dari atau sama dengan  $y
```

### 3.8 Opearator kurang dari atau sama dengan " <= "

```php
$x <= $y // TRUE bila nilai $x kurang dari atau sama dengan $y
```

Semua operator perbandingan digunakan untuk membandingkan dua buah nilai numerik atau string. Output dari operasi ini adalah nilai ``TRUE`` atau ``FALSE``.


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

Statement if memungkinkan kita untuk membuat percabangan kondisional. Jika Anda meletakkan kondisi di dalam () setelah if, code diantara tanda kurung { } akan dijalankan hanya jika kondisi benar. Gambar di bawah menunjukkan bagaimana statement if ditulis.

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



