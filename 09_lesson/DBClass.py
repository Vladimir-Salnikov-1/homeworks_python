from sqlalchemy import create_engine, inspect, text
from faker import Faker


class DBPage:
    def __init__(self, db_connection_string):
        self.engine = create_engine(db_connection_string)

    # Возвращает список таблиц в базе данных
    def get_table_names(self):
        with self.engine.connect():
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
                sql_request = text(
                    "INSERT INTO users(user_email) VALUES (:email)"
                    )
                connection.execute(sql_request, {"email": email})
                transaction.commit()
            except Exception as e:
                transaction.rollback()
                raise e

    # Удаляет пользователя с указанным email
    def delete_user(self, email):
        with self.engine.connect() as connection:
            transaction = connection.begin()
            try:
                sql_request = text(
                    "DELETE FROM users WHERE user_email = :email"
                    )
                connection.execute(sql_request, {"email": email})
                transaction.commit()
            except Exception as e:
                transaction.rollback()
                raise e

    # Обновляет email пользователя
    def update_user_email(self, old_email, new_email):
        with self.engine.connect() as connection:
            transaction = connection.begin()
            try:
                sql_request = text(
                    "UPDATE users SET user_email = :new_email \
                        WHERE user_email = :old_email"
                    )
                connection.execute(sql_request, {
                    "new_email": new_email,
                    "old_email": old_email
                    })
                transaction.commit()
            except Exception as e:
                transaction.rollback()
                raise e

    def create_fake_email(self):
        fake = Faker()
        fake_email = fake.email()
        return fake_email
