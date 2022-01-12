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
        // set the PDO error mode to exception
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        // $conn->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_OBJ);
        return $conn;
        
    } catch (PDOException $e) {
        echo "Connection failed: " . $e->getMessage();
    }
    return $conn;
}
