import pytest
from yougileApi import YougileApi


@pytest.fixture
def api():
    return YougileApi()


@pytest.mark.positive
@pytest.mark.create
def test_create_project(api):
    # Создание проекта с названием
    title = "HomeWork 8"
    new_project = api.create_project(title)
    assert new_project.status_code in [200, 201], (
        f"Ожидаем статус 200/201, получен {new_project.status_code}"
    )
    res = new_project.json()
    id = res["id"]
    # Поиск проекта по id
    search = api.get_project_by_id(id)
    data_search = search.json()
    # Проверить название
    assert data_search["title"] == title
    assert data_search["id"] == id


@pytest.mark.positive
@pytest.mark.edit
def test_edit_project(api):
    # Создаем проект
    title = "Название проекта"
    new_project = api.create_project(title)
    assert new_project.status_code in [200, 201], (
        f"Ожидаем статус 200/201, получен {new_project.status_code}"
    )
    id = new_project.json()["id"]
    # Меняем название
    new_title = "Новое название проекта"
    result = api.edit_project(id, new_title)
    # Проверяем статус и новое название
    assert result.status_code == 200
    # Поиск проекта по id
    search = api.get_project_by_id(id)
    data_search = search.json()
    # Проверить название
    assert data_search["title"] == new_title


@pytest.mark.positive
@pytest.mark.get
def test_get_project_by_id(api):
    # Создаем проект
    title = "Название проекта"
    new_project = api.create_project(title)
    assert new_project.status_code in [200, 201], (
        f"Ожидаем статус 200/201, получен {new_project.status_code}"
    )
    id = new_project.json()["id"]
    # Поиск проекта по id
    search = api.get_project_by_id(id)
    data_search = search.json()
    # Проверить название и id
    assert data_search["title"] == title
    assert data_search["id"] == id


@pytest.mark.negative
@pytest.mark.create
def test_create_project_without_title(api):
    # Создание проекта без названия
    title = ""
    result = api.create_project(title)
    assert result.status_code in [400], (
        f"Ожидаем статус 400, получен {result.status_code}"
    )
    result.json()


@pytest.mark.negative
def test_get_project_by_fake_id(api):
    # Получение проекта по несуществующему ID (формат UUID)
    fake_id = "00000000-0000-0000-0000-000000000000"
    resp = api.get_project_by_id(fake_id)
    assert resp.status_code == 404  # Not Found


@pytest.mark.negative
@pytest.mark.edit
def test_edit_project_empty_title(api):
    # Изменение названия на пустое
    # Создаем проект
    title = "Название проекта"
    new_project = api.create_project(title)
    assert new_project.status_code in [200, 201], (
        f"Ожидаем статус 200/201, получен {new_project.status_code}"
    )
    id = new_project.json()["id"]
    edit_resp = api.edit_project(id, "")
    assert edit_resp.status_code == 400
