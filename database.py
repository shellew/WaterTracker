import sqlite3
from WaterTracker.config import DATABASE

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS water_intake (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount INTEGER NOT NULL,
                timestamp TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_goal (
                id INTEGER PRIMARY KEY CHECK (id = 1),
                daily_goal INTEGER NOT NULL
            )
        ''')
        cursor.execute("INSERT OR IGNORE INTO user_goal (id, daily_goal) VALUES (1, 2000)")
        conn.commit()

def update_goal(daily_goal):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE user_goal SET daily_goal = ? WHERE id = 1", (daily_goal,))
        conn.commit()

def get_goal():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT daily_goal FROM user_goal WHERE id = 1")
        return cursor.fetchone()[0]
    
def record_intake(amount, timestamp):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO water_intake (amount, timestamp) VALUES (?, ?)", (amount, timestamp))
        conn.commit()

def get_today_intake(today_date):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(amount) FROM water_intake WHERE timestamp LIKE ?", (f"{today_date}%", ))
        return cursor.fetchone()[0] or 0
    
def get_history():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT amount, timestamp FROM water_intake ORDER BY timestamp DESC")
        return [{"amount": row[0], "timestamp": row[1]} for row in cursor.fetchall()]
    
def reset_intake():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM water_intake")
        conn.commit()