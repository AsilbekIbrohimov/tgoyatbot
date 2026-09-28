import sqlite3


class Database:
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

    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            email varchar(255),
            language varchar(3),
            trans int NOT NULL,
            reciter varchar(40) DEFAULT 'ar.alafasy',
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)
        # Eski bazalarga yangi ustunlarni qo'shamiz
        cols = [row[1] for row in self.execute("PRAGMA table_info(Users)", fetchall=True)]
        if "reciter" not in cols:
            self.execute(
                "ALTER TABLE Users ADD COLUMN reciter varchar(40) DEFAULT 'ar.alafasy'",
                commit=True,
            )
        if "text_ed" not in cols:
            self.execute(
                "ALTER TABLE Users ADD COLUMN text_ed varchar(40) DEFAULT 'local.sodiq'",
                commit=True,
            )

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, email: str = None, language: str = 'uz', trans: int = 0):
        # INSERT OR IGNORE: foydalanuvchi allaqachon bo'lsa xato bermaydi
        sql = """
        INSERT OR IGNORE INTO Users(id, Name, email, language, trans) VALUES(?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, email, language, trans), commit=True)

    def select_all_users(self):
        return self.execute("SELECT * FROM Users", fetchall=True)

    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def get_trans(self, id: int) -> int:
        """Foydalanuvchining tanlagan tarjimasi (0/1). Topilmasa 0."""
        row = self.execute(
            "SELECT trans FROM Users WHERE id = ?", parameters=(id,), fetchone=True
        )
        return row[0] if row else 0

    def get_reciter(self, id: int) -> str:
        """Foydalanuvchi tanlagan qori (edition id). Topilmasa standart."""
        row = self.execute(
            "SELECT reciter FROM Users WHERE id = ?", parameters=(id,), fetchone=True
        )
        return row[0] if row and row[0] else 'ar.alafasy'

    def update_user_reciter(self, reciter: str, id: int):
        return self.execute(
            "UPDATE Users SET reciter=? WHERE id=?", parameters=(reciter, id), commit=True
        )

    def get_text_ed(self, id: int) -> str:
        """Foydalanuvchi tanlagan matn edition'i. Topilmasa standart."""
        row = self.execute(
            "SELECT text_ed FROM Users WHERE id = ?", parameters=(id,), fetchone=True
        )
        return row[0] if row and row[0] else 'local.sodiq'

    def update_user_text_ed(self, text_ed: str, id: int):
        return self.execute(
            "UPDATE Users SET text_ed=? WHERE id=?", parameters=(text_ed, id), commit=True
        )

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_user_email(self, email, id):
        sql = "UPDATE Users SET email=? WHERE id=?"
        return self.execute(sql, parameters=(email, id), commit=True)

    def update_user_trans(self, trans, id):
        sql = "UPDATE Users SET trans=? WHERE id=?"
        return self.execute(sql, parameters=(trans, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)
