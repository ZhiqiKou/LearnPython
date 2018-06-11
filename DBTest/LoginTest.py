from MySqlHelper import MysqlHelper
from hashlib import sha1

# 接收用户输入信息
name = input('请输入用户名：')
pwd = input('请输入密码：')

# 对密码进行加密
s1 = sha1()
s1.update(pwd.encode('utf8'))
finally_pwd = s1.hexdigest()

# 根据用户名查询密码
sql = 'select passwd from users where name = %s'
sqlhelper = MysqlHelper('192.168.0.125', 3306, 'python3', 'root', '123456')
result = sqlhelper.query(sql, [name])

# 判断登录
if len(result) == 0:
    print('用户名错误！')
elif result[0][0] != finally_pwd:
    print('密码错误！')
else:
    print('登录成功！')
