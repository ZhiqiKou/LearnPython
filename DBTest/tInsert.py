import pymysql.cursors
try:
    conn = pymysql.connect(
        host='192.168.0.125',
        port=3306,
        user='root',
        passwd='123456',
        db='python3',
        charset='utf8'
    )
    cursor = conn.cursor()
    # 添加
    # sql = 'insert into students(name) values ("小明")'
    # 修改
    # sql = 'update students set name= "老王" where id=3'
    # 删除
    sql = 'delete from students where id=3'
    cursor.execute(sql)
    conn.commit()

    cursor.close()
    conn.close()
    print("操作完毕")
except Exception as e:
    print(e.messsage)

