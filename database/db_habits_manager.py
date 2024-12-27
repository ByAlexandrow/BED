import sqlite3


HABITS_DB_NAME = "db_habits.db"


def create_habits_db():
    """Создает таблицы в базе данных, если их нет."""
    connection = sqlite3.connect(HABITS_DB_NAME)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS habit_checkpoints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            habit_id INTEGER,
            year INTEGER,
            month INTEGER,
            day INTEGER,
            checked INTEGER DEFAULT 0,
            FOREIGN KEY (habit_id) REFERENCES habits (id)
        )
    """)
    connection.commit()
    connection.close()


def add_new_habit(name):
    """Добавляет новую привычку в базу данных или возвращает существующую."""
    connection = sqlite3.connect(HABITS_DB_NAME)
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM habits WHERE name = ?", (name,))
    result = cursor.fetchone()
    if result:
        habit_id = result[0]
    else:
        cursor.execute("INSERT INTO habits (name) VALUES (?)", (name,))
        habit_id = cursor.lastrowid
        connection.commit()

    connection.close()
    return habit_id


def add_habits_checkpoint(habit_id, year, month, day, checked=0):
    """Добавляет чекпоинт для привычки."""
    connection = sqlite3.connect(HABITS_DB_NAME)
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO habit_checkpoints (habit_id, year, month, day, checked)
        VALUES (?, ?, ?, ?, ?)
    """, (habit_id, year, month, day, checked))
    connection.commit()
    connection.close()


def get_all_habits():
    """Возвращает все привычки из базы данных."""
    connection = sqlite3.connect(HABITS_DB_NAME)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM habits")
    habits = cursor.fetchall()
    connection.close()
    return habits


def get_all_habits_checkpoints(habit_id, year, month):
    """Возвращает чекпоинты для конкретной привычки, года и месяца."""
    connection = sqlite3.connect(HABITS_DB_NAME)
    cursor = connection.cursor()
    cursor.execute("""
        SELECT day, checked FROM habit_checkpoints
        WHERE habit_id = ? AND year = ? AND month = ?
    """, (habit_id, year, month))
    checkpoints = cursor.fetchall()
    connection.close()
    return checkpoints


def update_checkpoint(habit_id, year, month, day, checked):
    """Обновляет состояние чекпоинта."""
    connection = sqlite3.connect(HABITS_DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id FROM habit_checkpoints
        WHERE habit_id = ? AND year = ? AND month = ? AND day = ?
    """, (habit_id, year, month, day))
    result = cursor.fetchone()

    if result:
        cursor.execute("""
            UPDATE habit_checkpoints
            SET checked = ?
            WHERE habit_id = ? AND year = ? AND month = ? AND day = ?
        """, (checked, habit_id, year, month, day))
    else:
        cursor.execute("""
            INSERT INTO habit_checkpoints (habit_id, year, month, day, checked)
            VALUES (?, ?, ?, ?, ?)
        """, (habit_id, year, month, day, checked))

    connection.commit()
    connection.close()


def delete_habit_from_db(habit_id):
    """Удаляет привычку и все её чекпоинты."""
    connection = sqlite3.connect(HABITS_DB_NAME)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM habits WHERE id = ?", (habit_id,))
    cursor.execute("DELETE FROM habit_checkpoints WHERE habit_id = ?", (habit_id,))
    connection.commit()
    connection.close()
