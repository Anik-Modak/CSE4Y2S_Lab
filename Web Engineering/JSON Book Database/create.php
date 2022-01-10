<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="UTF-8">
    <link rel="stylesheet" href="style.css">
    <title>Create</title>
</head>

<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {

	if (file_exists('books.json')) {
       	$booksJson = file_get_contents('books.json');
		$books = json_decode($booksJson, true);
    } else {
        $books = array();
    }

    if (isset($_POST['id'])){
        $id = $_POST['id'];
    }
    
    $flag = false;
    foreach ($books as $book) {
        if ($book['id'] == $id) {
            $flag = true;
        }
    }

    if($flag == true){
        header('Location: unique.php');
    }
    else{
         $data = array(
        'id' => $_POST['id'],
        'title' => $_POST['title'],
        'author' => $_POST['author'],
        'pages' => $_POST['pages'],
        'available' => $_POST['available'] === 'true' ? true : false,
        'isbn' => $_POST['isbn']
        );
        array_push($books, $data);
        $tmp = json_encode($books);
        file_put_contents('books.json', $tmp);
        header('Location: index.php');
    }
}
?>

<body>
    <ul class="sidenav">
      <li><a href="index.php">Home</a></li>
      <li><a class="active" href="create.php">Create</a></li>
      <li><a href="search.php">Search</a></li>
      <li><a href="about.php">About Me</a></li>
    </ul>

    <div class="content"> 
    <div class="flex-container" >
        <div class="book-obj">
            <h1 align="center">Insert a book information</h1>
            <form action="create.php" method="post">
            	<div class="flex-container input-group">
                    <label class="input-label" for="">Id:</label>
                    <input class="input-field" type="text" name="id" required>
                </div>
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
                    <input class="btn-submit" type="submit" value="Submit" required>
                </div>
            </form>
        </div>
    </div>
    </div>
</body>

</html>