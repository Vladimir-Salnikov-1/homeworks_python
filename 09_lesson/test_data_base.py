from DBClass import DBPage

# Настройка соединения
db_connection_string = "postgresql+psycopg://postgres:123@localhost:5432/postgres"
db_page = DBPage(db_connection_string)


# Тест на соединение с базой данных
def test_db_connection():
    table_names = db_page.get_table_names()
    required_tables = ['users', 'subject', 'student', 'group_student', 'teacher']
    for table in required_tables:
        assert table in table_names
    assert 'users' in table_names
    assert len(table_names) == 5

# Тест на запрос пользователей
def test_select():
    users = db_page.select_users()
    assert users[0]['user_id'] == 42568
    assert users[0]['user_email'] == "igorpetrov@mail.ru"
    assert len(users) > 1000


# Тест на добавление новой строки
def test_insert():
    test_email = "test_mail@mail.ru"
    db_page.insert_user(test_email)

    # Проверяем, что пользователь добавлен
    users = db_page.select_users()
    last_user = users[-1]['user_email']
    assert any(user['user_email'] == test_email for user in users)
    assert last_user == test_email
    db_page.delete_user(test_email)


# Тест на удаление строки
def test_delete():
    test_email = "test_mail@mail.ru"
    db_page.insert_user(test_email)
    db_page.delete_user(test_email)

    # Проверяем, что пользователь удален
    users = db_page.select_users()
    assert not any(user['user_email'] == test_email for user in users)


# Тест на изменение строки
def test_update():
    old_email = "test_mail@mail.ru"
    new_email = "test2_mail@mail.ru"
    db_page.insert_user(old_email)
    db_page.update_user_email(old_email, new_email)

    # Проверяем, что email обновлен
    users = db_page.select_users()
    last_user = users[-1]['user_email']
    assert any(user['user_email'] == new_email for user in users)
    assert last_user == new_email
    db_page.delete_user(new_email)
