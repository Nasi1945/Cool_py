import sqlite3

class Database:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS supermarket (id integer PRIMARY KEY,
                         name TEXT ,buyprice TEXT,sellprice TEXT,numbers TEXT)''')
        self.con.commit()
        
    def insert(self,name,buyprice,sellprice,numbers):
        self.cur.execute('''
                         INSERT INTO supermarket VALUES (NULL ,? , ? , ? , ?)
                         ''',(name,buyprice,sellprice,numbers))
        self.con.commit()
        
    def remove(self,id):
        self.cur.execute('DELETE FROM supermarket WHERE id = ?',(id,))
        self.con.commit()
        
    def fetch(self):
        self.cur.execute('SELECT * FROM supermarket order by name')
        row = self.cur.fetchall()
        return row
    
    def update(self,id,name,buyprice,sellprice,numbers):
        self.cur.execute("""
                         UPDATE supermarket SET name = ? , buyprice = ? , sellprice = ? , numbers = ? WHERE id = ?
                         """ , (name,buyprice,sellprice,numbers,id))
        self.con.commit()
        
    def search(self,name,buyprice,sellprice,numbers):
        self.cur.execute('SELECT * FROM supermarket WHERE name = ? or buyprice = ? or sellprice = ? or numbers = ?'
                         ,(name,buyprice,sellprice,numbers))
        recs = self.cur.fetchall()
        return recs
        
        
        
        
        
        
        
        
        