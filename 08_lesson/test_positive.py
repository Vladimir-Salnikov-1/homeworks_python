from classes.AuthorClass import Authtoris
from classes.ProjectClass import Project
from classes.Data_for_tests import Log


# Получить список компаний
def test_get_list_company_by_login():
    object = Authtoris()
    list_company = object.get_list_company_by_login(Log.log, Log.password)
    for company in list_company:
        assert "paging" in list_company
    for company in list_company:
        assert "content" in list_company
    paging = list_company["paging"]
    required_fields = ["limit", "offset", "next", "count"]
    for field in required_fields:
        assert field in paging, f"'{field}' отсутствует в 'paging'"
    content = list_company["content"]
    required_fields = ["id", "name", "isAdmin"]
    for project in content:
        for field in required_fields:
            assert field in project, f"'{field}' отсутствует в компании {company}"


# Получить список проектов
def test_get_list_project():
    object = Authtoris()
    key = object.get_key_of_company(Log.log, Log.password, 1)

    object2 = Project()
    list_projects = object2.get_list_projects(key)

    titles = [item['title'] for item in list_projects['content']]
    assert len(list_projects) >= 0
    assert len(titles) >= 0
    for project in list_projects:
        assert "paging" in list_projects
    for project in list_projects:
        assert "content" in list_projects
    paging = list_projects["paging"]
    required_fields = ["limit", "offset", "next", "count"]
    for field in required_fields:
        assert field in paging, f"'{field}' отсутствует в 'paging'"
    content = list_projects["content"]
    required_fields = ["id", "title", "timestamp"]
    for project in content:
        for field in required_fields:
            assert field in project, f"'{field}' отсутствует в проекте {project}"


# Создать проект
def test_create_project():
    object = Authtoris()
    key = object.get_key_of_company(Log.log, Log.password, 1)

    object2 = Project()
    new_project = object2.create_project("it's my life", key)
    name_last_project = object2.get_list_projects(key)["content"][-1]["title"]
    id_last_project = object2.get_list_projects(key)["content"][-1]["id"]

    assert name_last_project == "it's my life"
    assert "id" in new_project, "id отсутствует в ответе"
    object2.delete_project(id_last_project, key)


# Получить проект по id
def test_get_project_by_id():
    object = Authtoris()
    key = object.get_key_of_company(Log.log, Log.password, 1)

    object2 = Project()
    list_projects = object2.get_list_projects(key)
    id_last_project = list_projects["content"][-1]["id"]
    last_project = object2.get_project_by_id(id_last_project, key)

    assert last_project is not None
    required_fields = ["id", "title", "timestamp"]
    for fild in required_fields:
        assert fild in last_project


# Изменить название проекта
def test_change_title_project():
    object = Authtoris()
    key = object.get_key_of_company(Log.log, Log.password, 1)

    object2 = Project()
    new_project = object2.create_project("it's my life", key)
    list_projects = object2.get_list_projects(key)
    id_last_project = list_projects["content"][-1]["id"]
    changed_project = object2.change_title_project(id_last_project, "new title", key)
    change_title = object2.get_project_by_id(id_last_project, key)
    new_title = change_title["title"]

    assert new_title == "new title"
    assert new_project["id"] == changed_project["id"]
    object2.delete_project(id_last_project, key)


# Удалить проект
def test_delete_project():
    object = Authtoris()
    key = object.get_key_of_company(Log.log, Log.password, 1)

    new_project = Project()
    count_before = new_project.get_list_projects(key)["paging"]["count"]
    id_new_project = new_project.create_project("123", key)["id"]
    count_after_create = new_project.get_list_projects(key)["paging"]["count"]

    assert count_before == count_after_create - 1
    deleted_project = new_project.delete_project(id_new_project, key)
    count_after_delete = new_project.get_list_projects(key)["paging"]["count"]
    assert count_before == count_after_delete
    assert id_new_project == deleted_project["id"]
