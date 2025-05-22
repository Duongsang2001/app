import sqlite3 

class ClanModel:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute ("""
            CREATE TABLE IF NOT EXISTS clans 
                (
                name TEXT, 
                thanhvien INTEGER 
                )
            """)
        self.conn.commit()
        

    def add_clan(self, name):
        self.cursor.execute("""
            INSERT INTO clans (name) 
            VALUES (?)
        """,(name,))
        self.conn.commit()
        
        
        
    def insert_clan(self, name, thanhvien):
        self.cursor.execute ("""
            INSERT INTO clans (name, thanhvien) 
            VALUES (?, ?)
        """,(name, thanhvien))
        self.conn.commit()
        
        
    
    def kiem_tra(self):
        self.cursor.execute("""
                SELECT EXISTS(SELECT 1 FROM clans WHERE name IS NOT NULL AND name != '')
            """)
        result = self.cursor.fetchone()[0]  # Trả về 1 nếu có dữ liệu, 0 nếu không
        return bool(result)

    
    def get_nameHoi(self):
        self.cursor.execute("""
            SELECT name FROM clans
        """)
        data = self.cursor.fetchone()
        return data[0]
        
    def update_name(self,name):
        self.cursor.execute("""
            UPDATE clans
            SET name =?
        """,(name,))
        self.conn.commit()
