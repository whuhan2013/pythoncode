<?php 
require_once 'DBMysql.php';
$db = DBMysql::connect();
$sql = 'select * from stu order by rand() limit 2';
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
        .footer {
          position: absolute;
          bottom: 0;
          width: 100%;
          /* Set the fixed height of the footer here */
          height: 60px;
          background-color: #191E29;
          text-align: center;
          color: #DFDFDF;
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
      <div class="main">

        <div class="alert alert-info alert-dismissible" role="alert" hidden="">
          <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          <strong>!</strong>Of the two girls, who do you think is more beautiful~
        </div>

        <div class="progress">
            <div class="progress-bar" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="">
            <span class="">0% Complete</span>
            </div>
        </div>
        
        <div class="row">
            <?php 
                foreach ($results as $key => $value) {
             ?>
            <div class="col-sm-6 col-md-6 rankimg<?php echo $key; ?>">
                <input type="hidden" name="" value="<?php echo $value['id'] ?>">
                <a href="#" class="thumbnail" id="rank<?php echo $key; ?>">
                    <img src=" <?php echo $value['img'] ?> " alt="..." class="img-rounded">
                </a>
                <span><a href="#" title=""><?php echo $value['stu'] ?></a></span>
            </div>
            <?php } ?>
        </div>
      </div>
    </div><!-- /.container -->
    <footer class="footer">
      <div class="container">
        <p class="text-muted"><h4>Campus campus Belle ranking selection</h4><h5>www.shiyanlou.com</h5></p>
      </div>
    </footer>
    <script src="//cdn.bootcss.com/jquery/2.2.4/jquery.min.js"></script>
    <script>
        $(document).ready(function() {
            function getCookie(name) {
                var arr,reg=new RegExp("(^| )"+name+"=([^;]*)(;|$)");
                if(arr=document.cookie.match(reg)){
                    return (arr[2]);
                } else {
                    return null;
                }
            }
            if(!getCookie("rankwoman"))
            {
                $(".alert-info").show();
                document.cookie="rankwoman=rankwoman";
                document.cookie="rankwomanper=0";
            }
            var rankwomanper=parseInt(getCookie("rankwomanper"));
            $('#rank0').click(function() {
                $('#rank1').hide();
                rankwomanper=parseInt(getCookie("rankwomanper"))+1;
                document.cookie="rankwomanper="+rankwomanper;
                rank(0);
            });
            $('#rank1').click(function() {
                rankwomanper=parseInt(getCookie("rankwomanper"))+1;
                document.cookie="rankwomanper="+rankwomanper;
                $('#rank0').hide();
                rank(1);
            });
            function rank(i) {
                $.post('./Rank.php', {stu1: $('.rankimg0 input').val(),stu2:$('.rankimg1 input').val(),vid:i}, function(data, textStatus, xhr) {
                    if (textStatus == 'success') {
                        window.location.reload();
                    }
                });
            }
            if(getCookie("rankwomanper")>9){
                window.location.href="./ranklist.php";
            } else {
                $(".progress-bar").width(rankwomanper+"0%");
                $(".progress-bar span").text(rankwomanper+"0% Competed");
            }
        });
    </script>
</body>
</html>