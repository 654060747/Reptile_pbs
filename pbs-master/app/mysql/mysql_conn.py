#coding=utf-8
#!/usr/bin/python

import pymysql


# 打开数据库连接
db = pymysql.connect('127.0.0.1', 'root', 'llg911025', 'user')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor();

# # 如果数据表已经存在使用 execute() 方法删除表。
# cursor.execute("DROP TABLE IF EXISTS pythons");

# # 创建数据表SQL语句
# sql = "CREATE TABLE pythons (id INT auto_increment primary key not null,phone  CHAR(20) NOT NULL,user_name  CHAR(20),age INT,  address CHAR(1))"

insert_sql = [('121', 'juhty', 20, 'M'),('154154', '435gh', 20, 'Z'),('154154', '435gh', 20, 'Z')]
# print(str(insert_sql).split("[")[1].split("]")[0])
# print(str(insert_sql).replace('[','').replace(']',''))
# SQL 插入语句
sql = "INSERT INTO pythons (phone, user_name, age, address) VALUES "+str(insert_sql).split("[")[1].split("]")[0]
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # Rollback in case there is any error
   # 如果发生错误则回滚
   db.rollback()

cursor.close()
db.close()