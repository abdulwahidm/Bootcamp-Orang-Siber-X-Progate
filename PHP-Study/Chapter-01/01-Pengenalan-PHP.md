# Apa Itu PHP?

Dengan HTML, ada limitasi bagaimana kita mengontrol apa yang ditampilkan. Dengan menggunakan PHP, Anda dapat mengubah teks yang ditampilkan tergantung audiens dan situasi.

## Bagaimana Menulis PHP Code

Code PHP dapat tertanam di dalam HTML. Dengan menggunakan tag PHP spesial ```<?php ... ?>,``` Anda dapat menulis instruksi didalamnya. Code yang ditulis di dalam ```<?php ... ?>``` akan diubah menjadi HTML dan ditampilkan.

## Sintaksis PHP

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

### Variable

Variable diibaratkan kotak untuk menyimpan data. Kita mendefinisikan variable dengan menambah simbol $ diawal. Semua tipe data dapat disimpan menggunakan sintaksis ```$variableName = nilai;```. Dalam pemrograman, ```= `` artinya untuk menentukan nilai di kanan pada apa yang terletak di sebelah kiri.  

```php
<?php 
    $name = 'John'; // menyimnpan John ke variable name

    echo $name; // Hasil John
?>
```

### Penggabungan String

1. Penggabungan string dengan operator dot(.)

```php
    $lesson = 'PHP';
    echo $lesson.'Pemula';
    // Hasil: PHP Pemula

    $level = 'Pemula';
    echo $lesson.$level;
    // Hasil: PHP Pemula
```

2. Penggabungan string dengan substistusi variable

```php
    $name = 'Ninja Ken';
    echo "Halo {$name}"; 
    // Hasil: Halo, Ninja Ken

    echo 'Halo, {$name}';
    // Hasil: Halo, {$name}
    // {$name} tidak dicetak sebagai variable dari string
    // karena pada cara substitusi variable harus menggunakan double quote
```


