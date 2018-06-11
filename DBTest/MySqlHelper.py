import pymysql.cursors

class MysqlHelper(object):
    def __init__(self, host, port, db, user, passwd,charset='utf8'):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset

    def open(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.passwd,
            db=self.db,
            charset=self.charset
        )
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def cud(self, sql, params):
        '''增加，修改，删除'''
        try:
            self.open()
            self.cursor.execute(sql, params)
            self.conn.commit()
            self.close()
        except Exception as e:
            print(e.message)
        print('操作完成！')
    def query(self, sql, params):
        '''查询'''
        try:
            self.open()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchall()
            self.close()
            return result
        except Exception as e:
            print(e.message)
