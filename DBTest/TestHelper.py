import MySqlHelper

# 修改
# name = input('请输入学生姓名：')
# id = input('请输入学生编号：')
#
# sql = 'update students set name = %s where id = %s'
# params = [name, id]
# sqlhelper = MySqlHelper.MysqlHelper('192.168.0.125', 3306, 'python3', 'root', '123456')
# sqlhelper.cud(sql, params)

# 查询
sql = 'select id,name from students where id <= 2'
sqlhelper = MySqlHelper.MysqlHelper('192.168.0.125', 3306, 'python3', 'root', '123456')
print(sqlhelper.query(sql, None))