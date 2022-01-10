<?php

function isAvailable(array $book) 
{
	if (!$book['available']) {
		$result = ' <b> No </b>';
	}
	else{
		$result = ' <b> Yes </b>';
	}
	return $result;
}