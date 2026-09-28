import sqlite3


class Database2:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_messages(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Messages (
            message_id int NOT NULL,
            user_id int NOT NULL,
            PRIMARY KEY (message_id)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_message(self, message_id: int, user_id: int):
        sql = "INSERT OR IGNORE INTO Messages(message_id, user_id) VALUES(?, ?)"
        self.execute(sql, parameters=(message_id, user_id), commit=True)

    def select_message(self, **kwargs):
        sql = "SELECT * FROM Messages WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_messages(self):
        return self.execute("SELECT COUNT(*) FROM Messages;", fetchone=True)
