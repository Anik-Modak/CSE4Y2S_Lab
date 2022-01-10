<?php require_once 'functions.php'; ?>

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="style.css">
<title>Search Result</title>
</head>

<body>

<?php
	if (isset($_POST['id'])){
		$id = $_POST['id'];
	}

	if (file_exists('books.json')) {
       	$booksJson = file_get_contents('books.json');
				$books = json_decode($booksJson, true);
  } else {
      $books = array();
  }

  $flag = false;
  foreach ($books as $book) {
    if ($book['id'] == $id) {
    	$result = $book;
    	$flag = true;
    }
  }

  if($flag == false)
  	header('Location: 404.php');
?>

<ul class="sidenav">
  <li><a href="index.php">Home</a></li>
  <li><a href="create.php">Create</a></li>
  <li><a href="search.php">Search</a></li>
  <li><a href="about.php">About Me</a></li>
  <li><a class="active" href="show.php">Search Result</a></li>
</ul>

<div class="content">
<h1 align = "center"> Showing Search Result </h1>
<table align="center" border="2">
	<tr>
		<th> Id </th>
		<th> Title </th>
		<th> Author </th>
		<th> Pages </th>
		<th> Available </th>
		<th> Isbn </th>
	</tr>
	<tr>
		<td>
			<?php echo $result['id']; ?>
		</td>
		<td>
			<?php echo $result['title']; ?>
		</td>
		<td>
			<?php echo $result['author']; ?>
		</td>
		<td>
			<?php echo $result['pages']; ?>
		</td>
		<td>
			<?php echo isAvailable($result); ?>
		</td>
		<td>
			<?php echo $result['isbn']; ?>
		</td>
	</tr>
</table>
</div>
</body>
</html>