import sqlite3

class ThanhtichModel:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS thanhtich (
                htxsnv INTEGER,
                httnv INTEGER,
                htnv INTEGER,
                khtnv INTEGER
            )
        ''')
        self.conn.commit()
        
        
    def add_thanhtich(self, htxsnv, httnv, htnv, khtnv):
        self.cursor.execute('''
            INSERT INTO thanhtich (htxsnv, httnv, htnv, khtnv) VALUES (?, ?, ?, ?)
        ''', (htxsnv, httnv, htnv, khtnv))
        self.conn.commit()
        

    def update_thanhtich(self,htxsnv, httnv, htnv, khtnv):
        self.cursor.execute("""
        UPDATE thanhtich
        SET htsxnv =?, httnv = ?, htnv = ?, khtnv = ?
        """,(htxsnv,httnv,htnv,khtnv,))
        self.conn.commit()
        

    def get_thanhtich(self, ):
        self.cursor.execute("""
            SELECT * FROM thanhtich W
        """)
        data = self.cursor.fetchall()
        return data