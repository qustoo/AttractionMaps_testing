import sqlite3


class PhotoDatabase:
    # Конструктор по пути
    def __init__(self, path_to_db="photo.db"):
        self.path_to_db = path_to_db

    # Создаем подключение
    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    # функция есть sql - запрос, где id - основной ключ
    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = tuple()
        connection = self.connection

        # поиск ошибков и просмотр действий бд
        connection.set_trace_callback(logger)
        # позволяет делать запросы к бд
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        # если изменяли то изменяем бд
        if commit:
            # изменение бд
            connection.commit()

        # если выгружали данные то изменяем бд
        if fetchone:
            # выгружаем один тьюпл
            data = cursor.fetchone()

        # если выгружали все данные то бд
        if fetchall:
            # выгружаем всех в  тьюпл
            data = cursor.fetchall()

        # закрываем конешкн после изменений
        connection.close()
        return data

    # Функция создания таблицы фотографий
    # Основным ключом является имя файла
    def create_table_photos(self):
        # Photo - таблица фотографий
        sql = """
        CREATE TABLE IF NOT EXISTS Photos (
        filename VARCHAR(255) NOT NULL,
        name VARCHAR(255) NOT NULL,
        region VARCHAR(255),
        lat DOUBLE,
        lon DOUBLE,
        PRIMARY KEY (filename)
        );
        """
        # Закрепляем изменения
        self.execute(sql, commit=True)

    def add_photo(self, filename: str, name: str, region: str = None, lat: float = 0, lon: float = 0):
        sql = "INSERT INTO Photos(filename, name, region, lat, lon) VALUES(?, ?, ?, ?, ?)"
        self.execute(sql, (filename, name, region, lat, lon), commit=True)

    def select_all_photos(self):
        sql = "SELECT * FROM Photos"
        # Выгружаем все данные из таблицы
        return self.execute(sql, fetchall=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f" {item} = ?" for item in parameters.keys()
        ])
        return sql, tuple(parameters.values())

    def select_photos(self, **kwargs):
        sql = "SELECT * FROM Photos WHERE "
        # формируем запрос sql и формируем параметры из тьюпла
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchall=True)

    def count_photos(self):
        return self.execute("SELECT COUNT(*) FROM Photos", fetchone=True)

    def update_name(self, filename: str, name: str):
        sql = "UPDATE Photos SET name=? WHERE filename=?"
        return self.execute(sql, parameters=(name, filename), commit=True)

    def update_region(self, filename: str, region: str):
        sql = "UPDATE Photos SET region=? WHERE filename=?"
        return self.execute(sql, parameters=(region, filename), commit=True)

    def update_lat(self, filename: str, lat: float):
        sql = "UPDATE Photos SET lat=? WHERE filename=?"
        return self.execute(sql, parameters=(lat, filename), commit=True)

    def update_lon(self, filename: str, lon: float):
        sql = "UPDATE Photos SET lon=? WHERE filename=?"
        return self.execute(sql, parameters=(lon, filename), commit=True)

    def delete_all_photos(self):
        # Удаляем всех
        self.execute("DELETE FROM Photos WHERE True", commit=True)

    def delete_photo_by_filename(self, filename: str):
        sql = "DELETE FROM Photos WHERE filename=?"
        return self.execute(sql, parameters=tuple([filename]), commit=True)


# логгирование результатов
def logger(statement):
    print(f"""
_____
Executing in second DB:
{statement}
-----
""")
