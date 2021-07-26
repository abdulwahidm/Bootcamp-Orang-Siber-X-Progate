<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Progate</title>
  <link rel="stylesheet" type="text/css" href="stylesheet.css">
</head>
<body>

  
  <?php
    $name = 'Ninja Ken';
    // Cetak "Halo, ____" menggunakan variable $name.
    echo 'Halo, '.$name; // Cara 1 penggabungan String
  ?>

  <br>

  <?php

    $greeting = 'Selamat datang';
    echo "{$greeting}, {$name}"; // Cara 2 penggabungan String dengan double quote

  ?>

</body>
</html>
