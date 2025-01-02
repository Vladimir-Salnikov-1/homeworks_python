from classes.AuthtorizationClass import Authtorization
from classes.ProjectClass import Project
from classes.Data_for_tests import Log


# Создать проект с неверным типом данных в названии
def test_create_project_wrong_data_type_in_title():
    object = Authtorization()
    key = object.get_key_of_company(Log.log, Log.password, 1)

    object2 = Project()
    new_project = object2.create_project(123, key)
    assert new_project['statusCode'] == 400
    assert new_project['message'][0] == "title must be a string"


# Получить проект по неверному id
def test_get_project_by_wrong_id():
    object = Authtorization()
    key = object.get_key_of_company(Log.log, Log.password, 1)

    object2 = Project()
    project = object2.get_project_by_id("gkfllfkkfll,mkgkkfll", key)
    assert project['statusCode'] == 404
    assert project['message'] == 'Проект не найден'


# Получить список проектов с неверным ключом
def test_get_list_project_with_wrong_key():
    object2 = Project()
    list_project = object2.get_list_projects(None)
    assert list_project['statusCode'] == 401
    assert list_project['message'] == 'Unauthorized'


# Изменить название проекта указав неверный тип данных в названии
def test_change_title_with_wrong_type_new_title():
    object = Authtorization()
    key = object.get_key_of_company(Log.log, Log.password, 1)

    object2 = Project()
    object2.create_project("it's my life", key)
    list_projects = object2.get_list_projects(key)
    id_last_project = list_projects["content"][-1]["id"]
    new_title = object2.change_title_project(id_last_project, 1223, key)
    assert new_title['statusCode'] == 400
    assert new_title['message'][0] == 'title must be a string'
    object2.delete_project(id_last_project, key)


# Удалить проект с несуществующим id
def test_delete_project_with_wrong_id():
    object = Authtorization()
    key = object.get_key_of_company(Log.log, Log.password, 1)

    object2 = Project()
    new_project = object2.create_project("it's my life", key)
    id_new_project = new_project["id"]
    resp = object2.delete_project("none id", key)
    assert resp['statusCode'] == 404
    assert resp['message'] == 'Проект не найден'
    object2.delete_project(id_new_project, key)
