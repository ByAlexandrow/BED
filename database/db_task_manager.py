import sqlite3


def create_tasks_db():
    """Создаёт базу данных и таблицу для задач."""
    conn = sqlite3.connect('db_tasks.db')
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


def add_tasks_to_tasks_db(name, description):
    """Добавляет задачу в базу данных."""
    conn = sqlite3.connect('db_tasks.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (name, description) VALUES (?, ?)', (name, description))
    conn.commit()
    conn.close()


def load_tasks_from_tasks_db():
    """Загружает задачи из базы данных."""
    conn = sqlite3.connect('db_tasks.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, description FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return tasks


def update_tasks_in_tasks_db(old_name, new_name, old_description, new_description):
    """Обновляет задачу в базе данных."""
    conn = sqlite3.connect('db_tasks.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET name = ?, description = ? WHERE name = ? AND description = ?', (new_name, new_description, old_name, old_description))
    conn.commit()
    conn.close()


def delete_tasks_from_tasks_db(task_name):
    """Удаляет задачу из базы данных."""
    conn = sqlite3.connect('db_tasks.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE name = ?', (task_name,))
    conn.commit()
    conn.close()
