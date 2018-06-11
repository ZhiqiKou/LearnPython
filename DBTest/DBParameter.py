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
    name = input('请输入要添加的名字：')
    # 添加
    sql = 'insert into students(name) values (%s)'
    cursor.execute(sql, [name])
    conn.commit()

    cursor.close()
    conn.close()
    print("操作完毕")
except Exception as e:
    print(e.messsage)

