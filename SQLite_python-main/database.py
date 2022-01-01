import sqlite3

class connect:
    def __init__(self):
        self.conn = sqlite3.connect('dbcore.db')
        self.cur = self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

    def show_all(self):
        self.cur.execute("SELECT * FROM data")
        items = self.cur.fetchall()
        for item in items:
            print(item)
        self.commit()


    def add_one(self,id,first,last):
        self.cur.execute("INSERT INTO data VALUES('{id}','{f}','{l}')".format(id = id, f = first, l = last))
        self.commit()
        print("all jobs done!")


    def delete(self,id):
        self.cur.execute("DELETE FROM data WHERE id = '{}'".format(id))
        self.commit()

    def update(self,op,new,id):
        self.cur.execute("UPDATE data SET {o} = '{n}' WHERE id = {i}".format(o = op,n = new, i = id))
