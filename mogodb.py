import pymongo
from pprint import pprint
item = {
	'minexs':'xs',
	'bookname':'bookname',
	'id':'id',
	'chaptername':'chaptername',
	'chapter':'chapter'
}
conns = pymongo.MongoClient()
conn = conns.xs.dxs
conn = conn.insert(item) #MongoDB数据库只有在插入数据后才会真正创建。也就是说数据库创建集合（数据表）后，必须再插入一个文档（记录），数据库才创建完成。
# x = conn.delete_many({})
# print(x.deleted_count,'文档已删除')
# [print(y) for y in conn.find() ]
print(conns.list_database_names())