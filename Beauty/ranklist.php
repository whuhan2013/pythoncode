<?php 
require_once 'DBMysql.php';
$db = DBMysql::connect();
$sql = "SELECT * FROM `stu` ORDER BY `score` DESC";
$result = $db->query($sql);
while ($row = $result->fetch_assoc()) {
    $results[] = $row;
}
 ?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Campus campus Belle ranking selection</title>
    <link rel="stylesheet" href="//cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="//cdn.bootcss.com/jquery/2.2.4/jquery.min.js"></script>
    <style type="text/css" media="screen">
        body {
          padding-top: 50px;
        }
        .main {
          padding: 40px 15px;
          text-align: center;
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <a class="navbar-brand" href="http://www.shiyanlou.com">Campus Belle ranking (shiyanlou.com)</a>
      </div>
    </nav>
    <div class="container">        
        <table class="table table-hover">
          <caption>美女颜值排行表</caption>
          <thead>
            <tr>
              <th>Section</th>
              <th>Name</th>
              <th>RankScore</th>
            </tr>
          </thead>
          <tbody>
          <?php foreach ($results as $key => $value) {  ?>
            <tr>
              <th scope="row"><?php echo $key+1 ?></th>
              <td><a href="#" title=""><?php echo $value['stu'] ?></a></td>
              <td><?php echo $value['score'] ?></td>
            </tr>
            <?php } ?>
          </tbody>
        </table>
        <button class="btn btn-success" id="rechoose" style="float: right">Choose Again</button>
    </div><!-- /.container -->
    <script src="//cdn.bootcss.com/jquery/2.2.4/jquery.min.js"></script>
    <script type="text/javascript">
    $("#rechoose").on("click",function(){
       document.cookie="rankwomanper=0";
       window.location.href="./index.php";
    });
    </script>
    </body>
</html>