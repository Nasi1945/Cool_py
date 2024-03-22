import sqlite3

class Database:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS contact (id INTEGER PRIMARY KEY,
                         name TEXT, fname TEXT,address TEXT,phone TEXT)''')
        self.con.commit()
        
    def insert(self,name,fname,address,phone):
        self.cur.execute('''INSERT INTO contact VALUES (NULL,?,?,?,?)
                         ''',(name,fname,address,phone))
        self.con.commit()

    def remove(self,id):
        self.cur.execute('DELETE FROM contact WHERE id = ?',(id,))
        self.con.commit()
        
    def fetch(self):
        self.cur.execute('SELECT * FROM contact order by name')
        data = self.cur.fetchall()
        return data
    
    def update(self,name,fname,address,phone,id):
        self.cur.execute('''
                         UPDATE contact SET name = ? , fname = ? , address = ? , phone = ? WHERE id = ?
                         ''',(name,fname,address,phone,id))
        self.con.commit()
        
    def search(self,thing):
        self.cur.execute('SELECT * FROM contact WHERE id = ? or name = ? or fname = ? or address = ? or phone = ?',
                         (thing,thing,thing,thing,thing))
        searched = self.cur.fetchall()
        return searched
                         
                         
                         
                         
                         
                         
                         
        