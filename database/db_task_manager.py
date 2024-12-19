import sqlite3


def create_task_db():
    """Создаёт базу данных и таблицу для задач."""
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            completed BOOLEAN DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()


def add_task_to_task_db(name, description):
    """Добавляет задачу в базу данных."""
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (name, description) VALUES (?, ?)', (name, description))
    conn.commit()
    conn.close()


def load_tasks_from_task_db():
    """Загружает задачи из базы данных."""
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, description, completed FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return tasks


def update_task_in_task_db(old_name, new_name, old_description, new_description):
    """Обновляет задачу в базе данных."""
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET name = ?, description = ? WHERE name = ? AND description = ?', (new_name, new_description, old_name, old_description))
    conn.commit()
    conn.close()


def delete_task_from_task_db(task_name):
    """Удаляет задачу из базы данных."""
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE name = ?', (task_name,))
    conn.commit()
    conn.close()
