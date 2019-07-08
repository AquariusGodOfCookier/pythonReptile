import pymysql
import logging
import datetime
import json
import time
def conn(whats,whens):
    con=pymysql.connect(
        host='127.0.0.1',
        port=3308,
        user='',
        password='',
        db='pachong',
        charset='utf8'
        )
    cursor = con.cursor()
  # SQL 查询语句
    sql = "insert into boss (whats,whens) values('%s','%s')"%(whats,whens)
  # 执行SQL语句
    cursor.execute(sql)
    con.commit()
    con.close()
    cursor.close()
   # 获取所有记录列表
    return "AlertGradeSuccess"


# print(conn('php','2019-6-24 10:29'))
# print()