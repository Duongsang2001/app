import sqlite3

class ThanhVienModel:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS thanhvien1 (
                cccd TEXT PRIMARY KEY,
                fullname TEXT,
                nam_sinh INTEGER,
                cb TEXT,
                cvh TEXT,
                dv TEXT
                )
            """)
        self.conn.commit()
        
        
    def add_thanhvien(self, cccd, fullname, nam_sinh, cb,  cvh, dv):
            self.cursor.execute("""
                INSERT INTO thanhvien1 VALUES (?, ?, ?, ?, ?, ?)
                """, (cccd, fullname, nam_sinh, cb, cvh, dv))
            self.conn.commit()
        
    def search_thanhvien(self, column, value):
        query = f"SELECT * FROM thanhvien1 WHERE {column} COLLATE NOCASE = '{value}'"
        self.cursor.execute(query)
        return self.cursor.fetchall()
        
    def count_thanhvien(self):
            self.cursor.execute("""
                SELECT COUNT(*) FROM thanhvien1
                """)
            count = self.cursor.fetchone()[0]
            return count
    
    def Queries_hoitruong(self):
        self.cursor.execute("""
            SELECT * FROM thanhvien1 WHERE cvh COLLATE NOCASE = 'hội trưởng' 
            """)
        data = self.cursor.fetchall()
        return data

    def get_all_thanhvien(self):
        self.cursor.execute("""
            SELECT * FROM thanhvien1
            """)
        data = self.cursor.fetchall()
        return data
    
    def delete_person_model(self, cccd):
        query = "DELETE FROM thanhvien1 WHERE cccd = ?"
        self.cursor.execute(query, (cccd,))
        self.conn.commit()
