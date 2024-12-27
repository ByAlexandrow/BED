import sqlite3


DB_ACCOUNT_NAME = 'db_account.db'


def connect_db():
    """Подключается к базе данных и возвращает соединение."""
    conn = sqlite3.connect(DB_ACCOUNT_NAME)
    return conn


def create_account_db():
    """Создает таблицу accounts, если она не существует."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nickname TEXT,
            password TEXT,
            code INTEGER
        )
    ''')
    conn.commit()
    conn.close()


def add_account_data(nickname, password, code):
    """Добавляет новую запись в таблицу."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO accounts (nickname, password, code)
        VALUES (?, ?, ?)
    ''', (nickname, password, code))
    conn.commit()
    conn.close()


def update_data(nickname, password, code):
    """Обновляет существующую запись в таблице."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE accounts
        SET nickname = ?, password = ?, code = ?
        WHERE id = (SELECT id FROM accounts ORDER BY id DESC LIMIT 1)
    ''', (nickname, password, code))
    conn.commit()
    conn.close()


def delete_account_data(id):
    """Удаляет запись по ID."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM accounts WHERE id = ?
    ''', (id,))
    conn.commit()
    conn.close()


def get_all_account_data():
    """Возвращает последнюю запись из таблицы."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM accounts ORDER BY id DESC LIMIT 1')
    data = cursor.fetchone()
    conn.close()
    return data
