import sqlite3


def create_settings_db():
    conn = sqlite3.connect("settings.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings (
            id INTEGER PRIMARY KEY,
            selected_time TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def save_selected_time(time):
    conn = sqlite3.connect("settings.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM settings")
    if cursor.fetchone():
        cursor.execute("UPDATE settings SET selected_time = ?", (time,))
    else:
        cursor.execute("INSERT INTO settings (selected_time) VALUES (?)", (time,))
    conn.commit()
    conn.close()


def load_selected_time():
    conn = sqlite3.connect("settings.db")
    cursor = conn.cursor()
    cursor.execute("SELECT selected_time FROM settings")
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "15 minutes - default time"
