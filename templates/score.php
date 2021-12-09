<?php
if($_POST["thescore"])
{
	$score = $_POST["thescore"];
	// Here, you can also perform some database query operations with above values.
	echo "Hey you got ". $score ."!"; // Success Message
	//$db_connection = pg_connect("host=localhost dbname=pesuvariance user=postgres password=postgres");
	//$result = pg_query($db_connection, "INSERT INTO user_profile  lastname FROM employees");
}
?>