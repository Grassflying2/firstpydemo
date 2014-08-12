import MySQLdb
class userDb(object):
    def __init__(self):
        self.db = MySQLdb.connect(host='10.78.195.119', port=4000,
                                  user='root', passwd='123456', charset='utf8')
    def getUsers(self):
        cur = self.db.cursor()
        cur.execute('SELECT * from user u ')
        result = list(cur.fetchall())
        cur.close()
        self.db.close()
        return result

    def check(self, name, pwd):
        self.db.select_db('pydb')
        cur = self.db.cursor()
        cur.execute('SELECT count(*) from user u where u.name = "%s" and u.pwd = "%s"' % (name, pwd))
        num = cur.fetchone()
        return num[0]

    def setUser(self, name, pwd):
        self.db.select_db('pydb')
        cur = self.db.cursor()
        cur.execute('INSERT INTO user(name , pwd) VALUES("%s", "%s")' % (name, pwd))
        self.db.commit()
        return True

if __name__ == '__main__':
    userDb = userDb()
    print userDb.check('tj', 'tj')
