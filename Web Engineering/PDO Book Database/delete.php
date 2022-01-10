<?php
    require 'database/connection.php';
    require 'database/operation.php';
    $db = connect_db();

    if (isset($_GET['id'])) {
        $id = $_GET['id'];
        echo "$id";
        drop_data($db, $id);
        header('Location: index.php');
    } else {
        header('Location: 404.php');
    }
?>