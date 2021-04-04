import sqlite3


class Database:
    def __init__(self, path_to_db="mail.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = tuple()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id INT NOT NULL,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255),
        lat DOUBLE,
        lon DOUBLE,
        rating DOUBLE,
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)

    def add_user(self, id: int, name: str, email: str = None, lat: float = 0, lon: float = 0, rating: float = 0):
        sql = "INSERT INTO Users(id, name, email, lat, lon, rating) VALUES(?, ?, ?, ?, ?, ?)"
        self.execute(sql, (id, name, email, lat, lon, rating), commit=True)

    def select_all_users(self):
        sql = "SELECT * FROM Users"
        return self.execute(sql, fetchall=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f" {item} = ?" for item in parameters.keys()
        ])
        return sql, tuple(parameters.values())

    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users", fetchone=True)

    def update_email(self, id:int, email:str):
        sql = "UPDATE Users SET email=? WHERE id=?"
        return self.execute(sql, parameters=(email, id), commit=True)

    def update_rating(self, id:int, rating: float):
        sql = "UPDATE Users SET rating=? WHERE id=?"
        return self.execute(sql, parameters=(rating, id), commit=True)

    def update_lat(self, id:int, lat: float):
        sql = "UPDATE Users SET lat=? WHERE id=?"
        return self.execute(sql, parameters=(lat, id), commit=True)

    def update_lon(self, id:int, lon: float):
        sql = "UPDATE Users SET lon=? WHERE id=?"
        return self.execute(sql, parameters=(lon, id), commit=True)

    def delete_all_users(self):
        self.execute("DELETE FROM Users WHERE True", commit=True)

    def delete_user_by_id(self, id:int):
        sql = "DELETE FROM Users WHERE id=?"
        return self.execute(sql, parameters=tuple([id]), commit=True)

def logger(statement):
    print(f"""
_____
Executing:
{statement}
-----
""")