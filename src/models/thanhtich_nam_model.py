import sqlite3

class ThanhtichNamModel:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS thanhtichnam(
                nam TEXT PRIMARY KEY,
                note TEXT DEFAULT 'None'   
            )
    """)
        self.conn.commit()
        
    def insert_data(self, nam, note=None):
        if note is None:
            note = "Chào bạn"  # Giá trị mặc định
        self.cursor.execute("INSERT INTO thanhtichnam (nam, note) VALUES (?, ?)", (nam, note))
        self.conn.commit()


    

    def note_thanhtich(self, nam):
        self.cursor.execute("""
        SELECT * FROM thanhtichnam WHERE nam=?                          
    """,(nam,))
        exists_record = self.cursor.fetchone()
        if exists_record:
            return exists_record[1]
        
        
    
    def update_note(self, nam, note):
        self.cursor.execute("""
            UPDATE thanhtichnam
            SET note =?
            WHERE nam =?
            """,(nam,note,))
        self.conn.commit()