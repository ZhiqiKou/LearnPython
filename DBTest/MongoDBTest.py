from pymongo import *

# 获得客户端，建立连接
# 无安全认证
client = MongoClient('mongodb://192.168.0.125:27017')
# 有安全认证
# client = MongoClient('mongodb://用户名:密码@IP地址:27017/数据库名称')

# 切换数据库
db = client.py3
# 获取集合
stu = db.stu

# 增加
# stu.insert_one({'name': 'asd'})

# 修改
# stu.update_one({'name': 'asd'}, {'$set': {'name': '123'}})

# 删除
# stu.delete_one({'name': '123'})

# 查询
cursor = stu.find({'age': {'$gt': 20}}).skip(1).limit(1)
for s in cursor:
    print(s['name'])
