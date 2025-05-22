import sqlite3

class UserModel:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIARY KEY,
                username TEXT UNIQUE,
                email TEXT UNIQUE,
                password TEXT UNIQUE
                )                              
            """)
        self.conn.commit()
        

        
    def register_user(self, username, email, password):
        self.cursor.execute(
            "INSERT INTO users(username, email,password) VALUES(?,?,?)",(username, email,password)
            )
        self.conn.commit()
        
        
    def login_user(self, account,password):
        self.cursor.execute("""
            SELECT * FROM users
            WHERE (username=? OR email=?) AND password =?
            """, (account, account, password)
            )
        return self.cursor.fetchone()