<?php
function connect_db()
{
    $host = "sql6.freesqldatabase.com";
    $username = "sql6465206";
    $password = "QfaFhGgCLP";
    $dbname = "sql6465206";
    $port = "3306";
    
    try {
        $dsn ="mysql:host=$host;dbname=$dbname";
        $conn = new PDO($dsn, $username, $password);
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $conn;
    } catch (PDOException $e) {
        echo "Connection failed: " . $e->getMessage();
    }
    return $conn;
}
