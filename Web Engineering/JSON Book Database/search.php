<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="UTF-8">
    <link rel="stylesheet" href="style.css">
    <title>Search</title>
</head>

<body>
    <ul class="sidenav">
      <li><a href="index.php">Home</a></li>
      <li><a href="create.php">Create</a></li>
      <li><a class="active" href="search.php">Search</a></li>
      <li><a href="about.php">About Me</a></li>
    </ul>
    <div class="content"> 
    <div class="flex-container">
        <div class="book-obj">
            <h1 style="text-align: center;">Insert book Id for searching</h1>
            <form action="show.php" method="post">
            	<div class="flex-container input-group">
                    <label class="input-label" for="">Id: </label>
                    <input class="input-field" type="text" name="id" required>
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