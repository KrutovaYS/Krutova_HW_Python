import os
from dotenv import load_dotenv
from HW_bd_QAlesson import bd_QAlesson

# Загружаем переменные из .env
load_dotenv()

# Формируем строку подключения из .env
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME', 'QAlesson')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')

DB_CONNECTION = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
db = bd_QAlesson(DB_CONNECTION)


def test_add_subject():
    """Тест добавления предмета Anatomy"""
    title = "Anatomy"
    subject_id = db.add_subject(title)
    assert subject_id is not None

    subject = db.get_subject_by_title("Anatomy")
    assert subject is not None, "Предмет не найден"
    assert subject[1] == "Anatomy", "Название не совпадает"

    # Пост-обработка: удаление предмета
    delete = db.delete_subject(subject_id)
    assert delete is True, "Не удалось удалить"

    # Проверяем
    subject = db.get_subject_by_id(subject_id)
    assert subject is None, "Предмет все еще существует"


def test_update_subject_anatomy():
    """Тест изменения предмета Anatomy на New Anatomy"""
    # Добавляем предмет
    subject_id = db.add_subject("Anatomy")
    assert subject_id is not None

    # Изменяем название
    new_title = "New Anatomy"
    edit = db.update_subject_title(subject_id, new_title)
    assert edit is True, "Не удалось обновить"

    # Проверяем
    subject = db.get_subject_by_id(subject_id)
    assert subject[1] == new_title, "Название не изменилось"

    # Пост-обработка: удаление предмета
    db.delete_subject(subject_id)

    # Проверяем
    subject = db.get_subject_by_id(subject_id)
    assert subject is None, "Предмет все еще существует"


def test_delete_subject_anatomy():
    """Тест удаления предмета Anatomy"""
    # Добавляем предмет
    subject_id = db.add_subject("Anatomy")
    assert subject_id is not None

    # Удаляем
    result = db.delete_subject(subject_id)
    assert result is True, "Не удалось удалить"

    # Проверяем
    subject = db.get_subject_by_id(subject_id)
    assert subject is None, "Предмет все еще существует"
