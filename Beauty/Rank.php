<?php 
/**
* 排名算法
*/
class Rank
{
	private static $K = 32;
	private static $db;
	function __construct()
	{
		require_once 'DBMysql.php';
		self::$db = DBMysql::connect();
	}

	public function queryScore($id)
	{
		$sql = "SELECT * FROM stu WHERE `id` = $id";
		$info = mysqli_fetch_assoc(self::$db->query($sql));
		return $info['score'];
	}

	public function updateScore($Ra,$id)
	{
		self::$db->query("UPDATE `stu` SET `score` = $Ra WHERE `id` = $id");
	}

	public function expect($Ra,$Rb)
	{
		$Ea = 1/(1+pow(10,($Rb-$Rb)/400));
		return $Ea;
	}

	public function calculateScore($Ra,$Ea,$num)
	{
		$Ra = $Ra + self::$K*($num-$Ea);
		return $Ra;
	}

	public function selectStu()
	{
		$id1 = $_POST['stu1'];
		$id2 = $_POST['stu2'];
		$victoryid = $_POST['vid'];
		return $this->getScore($id1,$id2,$victoryid);
	}

	public function getScore($id1,$id2,$victoryid)
	{
		$Ra = $this->queryScore($id1);
		$Rb = $this->queryScore($id2);
		if ($Ra & $Rb) {
			$Ea = $this->expect($Ra, $Rb);
			$Eb = $this->expect($Rb, $Ra);
			$Ra = $this->calculateScore($Ra, $Ea, 1-$victoryid);
			$Rb = $this->calculateScore($Rb, $Eb, $victoryid);
			$Rab = array($Ra,$Rb);
			$this->updateScore($Ra, $id1);
			$this->updateScore($Rb, $id2);
			return $Rab;
		} else {
			return false;
		}
	}
}
$Rank = new Rank();
$Rank->selectStu();
