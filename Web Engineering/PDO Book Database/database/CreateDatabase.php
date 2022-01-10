<?php
function create_table($db)
{
    $db->query(
        'CREATE TABLE if not exists book( 
            id   INT AUTO_INCREMENT,
            title  VARCHAR(500), 
            author VARCHAR(500), 
            available  VARCHAR(500),
            pages   VARCHAR(500),
            isbn   VARCHAR(500),
            PRIMARY KEY(id)
        )'
    );
}