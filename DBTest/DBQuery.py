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
    # 查询单行数据
    #cursor.execute('select * from students where id=2')
    # result = cursor.fetchone()

    # 查询多行数据
    cursor.execute('select * from students')
    result = cursor.fetchall()

    print(result)
    cursor.close()
    conn.close()
    print("操作完毕")
except Exception as e:
    print(e.messsage)

