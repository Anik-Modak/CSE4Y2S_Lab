<?php
    require 'database/connection.php';
    require 'database/CreateDatabase.php';
    require 'database/operation.php';
    require 'functions.php';

    $db = connect_db();
    create_table($db);
    
    $query = isset($_GET['query']) ? $_GET['query'] : '';
    $size_of_query = strlen($query);
    if ($size_of_query != 0) {
        $books = search_data($db,$query);
    }
    else{
        $books =  show_all_data($db);
    }
    $books = $books->fetchAll(PDO::FETCH_ASSOC);
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="assets/style.css" type="text/css">

    <title> Book Store</title>
</head>

<body>

    <div class="container">
        <div class="row navbar">
            <div class="logo">
                <a href="<?php echo 'index.php' ?>" class="btn btn-lg btn-primary">Home</a>
            </div>
            <div class="search-container">
                <form class="example">
                    <div>
                        <input type="text" placeholder="Search by Title" name="query">
                        <button type="submit"><i class="fa fa-search"></i></button>
                    </div>
                </form>
            </div>
        </div>
    </div>


    <div class="container">
        <div class="row">
            <h1 > Showing All Data: </h1>
            <table>
                <tr>
                    <th>Id</th>
                    <th>Title</th>
                    <th>Author</th>
                    <th>Availablity</th>
                    <th>Pages</th>
                    <th>ISBN</th>
                    <th>Option</th>
                </tr>
                <?php foreach ($books as $key => $book): ?>
                <tr>
                    <td>
                        <?php echo  $key + 1; ?>
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
                        <a href="<?php echo 'delete.php?id=' .$book['id'];  ?>"> <button class="btn-lg btn-delete" onclick="return confirm('Are you sure you want to delete this?')">Delete</button></a>
                    </td>
                </tr>
                <?php endforeach; ?>
            </table>


            <?php if (sizeof($books) == 0) : ?>
                <h1 align="center"> Sorry, No item found!</h1>
            <?php endif; ?>

            <div class="create">
                <a href="<?php echo 'create.php' ?>">
                    <button class="btn-lg btn-submit">Create</button>
                </a>
            </div>
        </div>
    </div>

</body>

</html>
