from DBClass import DBPage

# Настройка соединения
db_connection_string = \
    "postgresql+psycopg://postgres:123@localhost:5432/postgres"
db_page = DBPage(db_connection_string)


# Тест на соединение с базой данных
def test_db_connection():
    table_names = db_page.get_table_names()
    required_tables = [
        'users', 'subject', 'student', 'group_student', 'teacher']
    for table in required_tables:
        assert table in table_names
    assert 'users' in table_names
    assert len(table_names) == len(required_tables)


# Тест на запрос пользователей
def test_select():
    users = db_page.select_users()
    required_fields = ['user_id', 'user_email', 'subject_id']

    for user in users:
        for field in required_fields:
            assert field in user
    assert users[0]['user_id'] == 42568
    assert users[0]['user_email'] == "igorpetrov@mail.ru"
    assert len(users) > 1000


# Тест на добавление новой строки
def test_insert():
    fake_email = db_page.create_fake_email()
    db_page.insert_user(fake_email)

    # Проверяем, что пользователь добавлен
    users = db_page.select_users()
    last_user = users[-1]['user_email']
    assert any(user['user_email'] == fake_email for user in users)
    assert last_user == fake_email, \
        "email последнего пользователя не совпадает с созданным email"
    db_page.delete_user(fake_email)


# Тест на удаление строки
def test_delete():
    test_email = db_page.create_fake_email()
    db_page.insert_user(test_email)
    db_page.delete_user(test_email)

    # Проверяем, что пользователь удален
    users = db_page.select_users()
    assert not any(user['user_email'] == test_email for user in users), \
        "Пользователь с таким email все еще существует"


# Тест на изменение строки
def test_update():
    old_email = db_page.create_fake_email()
    new_email = db_page.create_fake_email()
    db_page.insert_user(old_email)
    db_page.update_user_email(old_email, new_email)

    # Проверяем, что email обновлен
    users = db_page.select_users()
    last_user = users[-1]['user_email']
    assert any(user['user_email'] == new_email for user in users)
    assert last_user == new_email
    db_page.delete_user(new_email)
