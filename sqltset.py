#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql

# connection = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="00000000",
#     database="test",
#     charset="utf8",
#     cursorclass=pymysql.cursors.DictCursor)
connection = pymysql.connect(
    host="192.168.139.133",
    user="root",
    password="123456",
    database="xs",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor)

item = {
	'minexs':'xs',
	'bookname':'bookname',
	'id':'id',
	'chaptername':'chaptername',
	'chapter':'chapter'
}
ls = ['']
try: 
	with connection.cursor() as cursor:
		for x in ls:
			check_sql = '''drop table if exists `%(minexs)s`'''
			cursor.execute(check_sql, item)
			sql = '''
			create table `%(minexs)s`(
				`%(id)s` int unsigned auto_increment comment '记录id',
				`%(bookname)s` varchar(100) default '' comment '书名',
				`%(chaptername)s` varchar(100) default '' comment '章节',
				`%(chapter)s` text comment '内容',
				primary key(`%(id)s`)
			)engine=innodb default charset=utf8;
			'''
			cursor.execute(sql, item)
			
	connection.commit()
finally:
	connection.close()
print('Done with ',sql)
