import pymysql
pymysql.install_as_MySQLdb()
db=pymysql.connect("localhost","root","root","recommend")
cursor=db.cursor()
sql="create table user_anime(user int,anime int)"
cursor.execute(sql)
db.close()