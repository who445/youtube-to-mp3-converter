<?php
session_start();

// Ambil parameter 'page' dari URL
$page = isset($_GET['page']) ? $_GET['page'] : 'home'; // Default ke 'home' jika tidak ada parameter 'page'

// Tentukan path file berdasarkan parameter 'page'
$filePath = 'maincontent/' . $page . '.php';

// Periksa apakah file yang diminta ada
if (file_exists($filePath)) {
    include($filePath); // Menyertakan file konten yang sesuai
} else {
    // Menampilkan gambar dan pesan "Halaman Tidak Ditemukan"
    echo '<div class="not-found-container">';
    echo '<img src="img/404-not-found.webp" alt="404 Not Found" class="not-found-img"/>';
    echo '<h2>Halaman Tidak Ditemukan</h2>';
    echo '</div>';
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/not-found.css">
</head>
<body>
    
</body>
</html>
<br>
<br>
<br>
<?php
if (isset($_GET['page'])) {
    $page = $_GET['page'];

    switch ($page) {
        case 'home':
            break;
        case 'keranjang':
            break;
        case 'bantuan':
            break;
        case 'profile':
            break;
        case 'login':
            break;    
        case 'register': // Tambahkan case untuk register   
            break;
        default:
            echo "<h1>Halaman tidak ditemukan!</h1>";
            echo '<img src="img/404-not-found.webp" alt="404 Not Found" class="not-found-img"/>';
            break;
    }
}
?>