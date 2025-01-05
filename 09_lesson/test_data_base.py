from sqlalchemy import create_engine, inspect, text

db_connection_string = "postgresql+psycopg://postgres:123@localhost:5432/postgres"
db = create_engine(db_connection_string)


def test_db_connection():
    # Используем инспектор для получения информации о таблицах
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[1] == 'subject'

def test_select():
    connection = db.connect()  # Создаем соединение
    sql_request = text("select * from users")
    result = connection.execute(sql_request)
    rows = result.mappings().all()   # Получаем результат в виде словарей
    row1 = rows[0]

    assert row1['user_id'] == 42568
    assert row1['user_email'] == "igorpetrov@mail.ru"

    connection.close()      # Закрываем соединение

def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("INSERT INTO users(user_email) VALUES ('test_mail@mail.ru')")
    connection.execute(sql, {"new_name": "SkyPro"})
    

    transaction.commit()
    connection.close()

def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM users WHERE user_email = 'test_mail@mail.ru'")
    connection.execute(sql, {"id": 602})
   

    transaction.commit()
    connection.close()

def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("UPDATE users SET user_email = 'test2_mail@mail.ru' WHERE user_email = 'test_mail@mail.ru'")
    connection.execute(sql, {"descr": 'New descr', "id": 602})
    

    transaction.commit()
    connection.close()
