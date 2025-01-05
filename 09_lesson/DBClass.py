from sqlalchemy import create_engine, inspect, text


class DBPage:
    def __init__(self, db_connection_string):
        self.engine = create_engine(db_connection_string)

    # Возвращает список таблиц в базе данных
    def get_table_names(self):
        with self.engine.connect() as connection:
            inspector = inspect(self.engine)
            return inspector.get_table_names()

    # Получает всех пользователей из таблицы 'users'
    def select_users(self):
        with self.engine.connect() as connection:
            sql_request = text("SELECT * FROM users")
            result = connection.execute(sql_request)
            return result.mappings().all()

    # Добавляет пользователя с указанным email
    def insert_user(self, email):
        with self.engine.connect() as connection:
            transaction = connection.begin()
            try:
                sql = text("INSERT INTO users(user_email) VALUES (:email)")
                connection.execute(sql, {"email": email})
                transaction.commit()
            except Exception as e:
                transaction.rollback()
                raise e

    # Удаляет пользователя с указанным email
    def delete_user(self, email):
        with self.engine.connect() as connection:
            transaction = connection.begin()
            try:
                sql = text("DELETE FROM users WHERE user_email = :email")
                connection.execute(sql, {"email": email})
                transaction.commit()
            except Exception as e:
                transaction.rollback()
                raise e

    # Обновляет email пользователя
    def update_user_email(self, old_email, new_email):
        with self.engine.connect() as connection:
            transaction = connection.begin()
            try:
                sql = text("UPDATE users SET user_email = :new_email WHERE user_email = :old_email")
                connection.execute(sql, {"new_email": new_email, "old_email": old_email})
                transaction.commit()
            except Exception as e:
                transaction.rollback()
                raise e