import pymysql
import string
import random

KEY_LEN=20
KEY_ALL=200

def base_str():
    return (string.ascii_letters+string.digits)

def key_gen():
    keylist=[random.choice(base_str()) for i in range(KEY_LEN)]
    return ("".join(keylist))

def key_num(num,result=None):
    if result is None:
        result=[]
    for i in range(num):
        result.append(key_gen())
    return result

class mysql_init(object):
    def __init__(self,conn):
        self.conn=None

    def connect(self):
        self.conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="root",
        db="test",
        charset="utf8"
        )

if __name__ == "__main__":
    pymysql.install_as_MySQLdb()
    dbconn = mysql_init(None)
    dbconn.connect()