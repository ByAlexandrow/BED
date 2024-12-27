import sqlite3
from datetime import datetime

NOTES_DB_NAME = 'db_notes.db'

# Функция для подключения к базе данных
def get_db_connection():
    conn = sqlite3.connect(NOTES_DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


# Создание таблицы notes
def create_notes_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()


# Добавление заметки
def add_note(title, content):
    conn = get_db_connection()
    conn.execute('''
        INSERT INTO notes (title, content) VALUES (?, ?)
    ''', (title, content))
    conn.commit()
    conn.close()


# Обновление заметки
def update_note(note_id, title, content):
    updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn = get_db_connection()
    conn.execute('''
        UPDATE notes SET title = ?, content = ?, updated_at = ? WHERE id = ?
    ''', (title, content, updated_at, note_id))
    conn.commit()
    conn.close()


# Удаление заметки
def delete_note(note_id):
    conn = get_db_connection()
    conn.execute('''
        DELETE FROM notes WHERE id = ?
    ''', (note_id,))
    conn.commit()
    conn.close()


# Получение одной заметки по ID
def get_note(note_id):
    conn = get_db_connection()
    note = conn.execute('''
        SELECT * FROM notes WHERE id = ?
    ''', (note_id,)).fetchone()
    conn.close()
    return note


# Получение всех заметок
def get_all_notes():
    conn = get_db_connection()
    notes = conn.execute('''
        SELECT * FROM notes ORDER BY updated_at DESC
    ''').fetchall()
    conn.close()
    return notes
