<?php require_once 'functions.php'; ?>

<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="style.css">
<title>Home</title>
</head>

<body>
<?php
	$books = '';
	if (file_exists('books.json')) {
       	$booksJson = file_get_contents('books.json');
		$books = json_decode($booksJson, true);
    } else {
        $books = array();
    }
?>

<ul class="sidenav">
  <li><a class="active" href="index.php">Home</a></li>
  <li><a href="create.php">Create</a></li>
  <li><a href="search.php">Search</a></li>
  <li><a href="about.php">About Me</a></li>
</ul>

<div class="content">
<h1 align = "center"> Showing all book information from json file </h1>
<table align = "center" border="1">
	<tr class="row header">
		<th> Id </th>
		<th> Title </th>
		<th> Author </th>
		<th> Pages </th>
		<th> Available </th>
		<th> Isbn </th>
		<th> Operation </th>
	</tr>
	<?php foreach ($books as $key => $book): ?>
	<tr>
		<td>
			<?php echo $book['id']; ?>
		</td>
		<td>
			<?php echo $book['title']; ?>
		</td>
		<td>
			<?php echo $book['author']; ?>
		</td>
		<td>
			<?php echo $book['pages']; ?>
		</td>
		<td>
			<?php echo isAvailable($book); ?>
		</td>
		<td>
			<?php echo $book['isbn']; ?>
		</td>
		<td>
            <a href="delete.php?id=<?php echo $key+1?>." onClick="javascript:return confirm('are you sure you want to delete this?');">
                <button class="btn-delete"> Delete </button>
            </a>
        </td>
	</tr>
	<?php endforeach; ?>

</table>
</div>
</body>
</html>