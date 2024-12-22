import sqlite3


def create_tasks_db():
    """Создаёт базу данных и таблицу для задач."""
    conn = sqlite3.connect('db_tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,  -- Уникальное имя задачи
            description TEXT,
            level TEXT DEFAULT 'Легкий'  -- Уровень срочности по умолчанию
        )
    ''')
    conn.commit()
    conn.close()


def add_tasks_to_tasks_db(name, description, level="Легкий"):
    """Добавляет задачу в базу данных."""
    conn = sqlite3.connect('db_tasks.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (name, description, level) VALUES (?, ?, ?)', (name, description, level))
    conn.commit()
    conn.close()


def is_name_unique(task_name, task_id=None):
    """
    Проверяет, уникально ли имя задачи в базе данных.
    Возвращает True, если имя уникально, и False, если имя уже существует.
    Если task_id указан, исключает текущую задачу из проверки.
    """
    connection = sqlite3.connect("db_tasks.db")
    cursor = connection.cursor()

    if task_id:
        # Исключаем текущую задачу из проверки
        cursor.execute("SELECT COUNT(*) FROM tasks WHERE name = ? AND id != ?", (task_name, task_id))
    else:
        # Проверяем все задачи
        cursor.execute("SELECT COUNT(*) FROM tasks WHERE name = ?", (task_name,))

    count = cursor.fetchone()[0]
    connection.close()
    return count == 0


def get_task_id_by_name(task_name):
        """Возвращает идентификатор задачи по её имени."""
        connection = sqlite3.connect("db_tasks.db")
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM tasks WHERE name = ?", (task_name,))
        result = cursor.fetchone()
        connection.close()
        return result[0] if result else None


def load_tasks_from_tasks_db():
    """Загружает задачи из базы данных."""
    conn = sqlite3.connect('db_tasks.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, description, level FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return tasks


def update_tasks_in_tasks_db(old_name, new_name, old_description, new_description, new_level):
    """Обновляет задачу в базе данных."""
    conn = sqlite3.connect('db_tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE tasks 
        SET name = ?, description = ?, level = ? 
        WHERE name = ? AND description = ?
    ''', (new_name, new_description, new_level, old_name, old_description))
    conn.commit()
    conn.close()


def delete_tasks_from_tasks_db(task_name):
    """Удаляет задачу из базы данных."""
    conn = sqlite3.connect('db_tasks.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE name = ?', (task_name,))
    conn.commit()
    conn.close()


def get_task_level(task_name):
    """Возвращает уровень срочности задачи по имени."""
    conn = sqlite3.connect('db_tasks.db')
    cursor = conn.cursor()
    cursor.execute('SELECT level FROM tasks WHERE name = ?', (task_name,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None


def set_default_level(task_name):
    """Устанавливает уровень срочности задачи по умолчанию ('Легкий')."""
    conn = sqlite3.connect('db_tasks.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET level = ? WHERE name = ?', ('Легкий', task_name))
    conn.commit()
    conn.close()
