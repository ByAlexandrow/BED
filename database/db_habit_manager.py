import sqlite3


def create_habits_db():
    """Создаёт базу данных и таблицу для привычке."""
    conn = sqlite3.connect('habits.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()


def add_habits_to_habits_db(name, description):
    """Добавляет привычку в базу данных."""
    conn = sqlite3.connect('habits.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (name, description) VALUES (?, ?)', (name, description))
    conn.commit()
    conn.close()


def load_habits_from_habits_db():
    """Загружает привычки из базы данных."""
    conn = sqlite3.connect('habits.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, description FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return tasks


def update_habits_in_habits_db(old_name, new_name, old_description, new_description):
    """Обновляет привычки в базе данных."""
    conn = sqlite3.connect('habits.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET name = ?, description = ? WHERE name = ? AND description = ?', (new_name, new_description, old_name, old_description))
    conn.commit()
    conn.close()


def delete_habits_from_habits_db(task_name):
    """Удаляет привычку из базы данных."""
    conn = sqlite3.connect('habits.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE name = ?', (task_name,))
    conn.commit()
    conn.close()
