
<?php
    require 'database/connection.php';
    require 'database/operation.php';

    $db = connect_db();
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        add_data($db,$_POST['title'],$_POST['author'],$_POST['available'],$_POST['pages'],$_POST['isbn']);
        header('Location: index.php');
    }
?>


<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <link rel="stylesheet" href="assets/style.css" type="text/css">
    <title>Create </title>
</head>

<body>
    <div class="container">
        <div class="row navbar">
            <div class="logo">
                <a href="<?php echo 'index.php' ?>" class="btn btn-lg btn-primary">Home</a>
            </div>
        </div>
    </div>

    <div class="container" align="center" >
        <div class="book-obj">
            <h1 align="center">Insert a book information</h1>
            <form action="create.php" method="post">
                <div class="flex-container input-group">
                    <label class="input-label" for="">Title:</label>
                    <input class="input-field" type="text" name="title" required>
                </div>
                <div class="flex-container input-group">
                    <label class="input-label" for="">Author:</label>
                    <input class="input-field" type="text" name="author" required>
                </div>
                <div class="flex-container input-group">
                    <label class="input-label" for="">Availablity:</label>
                    <div class="flex-container" style="justify-content: start;">
                        <div><input type="radio" name="available" value="true" required> <b> True </b></div>
                        <div><input type="radio" name="available" value="false"> <b> False </b> </div>
                    </div>
                </div>
                <div class="flex-container input-group">
                    <label class="input-label" for="">Pages:</label>
                    <input class="input-field" type="text" name="pages" required>
                </div>
                <div class="flex-container input-group">
                    <label class="input-label" for="">ISBN:</label>
                    <input class="input-field" type="text" name="isbn" required>
                </div>
                <div class="flex-container" style="justify-content: center;">
                    <input class="btn-lg btn-submit" type="submit" value="Submit" required>
                </div>
            </form>
        </div>
    </div>
</body>
