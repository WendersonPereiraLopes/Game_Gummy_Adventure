import sqlite3

class ProxyDB:

    def __init__(self, name_db):
        self.name_db = name_db
        self.conn = sqlite3.connect(name_db)
        self.conn.execute('''
                            CREATE TABLE IF NOT EXISTS dados(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            score INTEGER NOT NULL,
                            date TEXT NOT NULL)
                          ''')
        
    def save_data(self,score_dict: dict):
        self.conn.execute('''
                            INSERT INTO dados(score, date)
                            VALUES (:score, :date)
                          ''', score_dict)
        self.conn.commit()

    def retrive_top5(self) -> list:
        return self.conn.execute('''
                                    SELECT * FROM dados 
                                    ORDER BY date DESC 
                                    LIMIT 5
                                ''').fetchall()

    def close(self):
        return self.conn.close()
    