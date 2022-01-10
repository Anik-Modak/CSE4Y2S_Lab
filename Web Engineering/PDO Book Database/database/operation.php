<?php
function add_data($db,$title,$author,$available,$pages,$isbn)
{
    $create = $db->query("INSERT INTO book( title, author,available,pages,isbn) values ('$title','$author','$available','$pages','$isbn');");
}
function drop_data($db, $id)
{
    $db->query("DELETE from book WHERE id IN( $id)");
}
function search_data($db,$str)
{
    $result =  $db->query("SELECT * FROM book WHERE title like('%$str%')");
    return $result;
}
function show_all_data($db)
{
    $result =  $db->query("SELECT * FROM book WHERE 1");
    return $result;
}

