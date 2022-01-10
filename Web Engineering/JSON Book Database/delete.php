<?php
if (isset($_GET['id'])) {
    $id = $_GET['id'];
    
    $books = '';
    if (file_exists('books.json')) {
        $booksJson = file_get_contents('books.json');
        $books = json_decode($booksJson, true);
    } else {
        $books = array();
    }

    if ((int)$id-1 < count($books)) {
        array_splice($books, $id-1, 1);
        $tmp  = json_encode($books);
        file_put_contents('books.json', $tmp);
        header('Location: index.php');
    } else {
        header('Location: 404.php');
    }
} else {
    header('Location: 404.php');
}
?>