<?php

class DBMysql
{
	public static function connect(){
		$dbc = new mysqli('localhost','root','','beauty') OR die('Could not connected to MySQL: '.mysql_error());
		$dbc->query('SET NAMES utf8');
		return $dbc;
	}
}

