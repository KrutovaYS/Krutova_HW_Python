from sqlalchemy import create_engine, text


class bd_QAlesson:
    # Класс для работы с базой данных QAlesson

    # Словарь с SQL-запросами
    __scripts = {
        "select_subject_by_title": text("""
        SELECT subject_id, subject_title
        FROM subject WHERE subject_title = :title
        """),
        "select_subject_by_id": text("""
        SELECT subject_id, subject_title
        FROM subject WHERE subject_id = :id
        """),
        "insert_subject": text("""
        INSERT INTO subject (subject_id, subject_title)
        VALUES (:id, :title)
        """),
        "update_subject": text("""
        UPDATE subject SET subject_title = :new_title
        WHERE subject_id = :id
        """),
        "delete_subject": text("""
        DELETE FROM subject WHERE subject_id = :id
        """),
        "check_subject_exists": text("""
        SELECT subject_id FROM subject
        WHERE subject_title = :title
        """),
        "get_max_id": text("SELECT MAX(subject_id) FROM subject")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def add_subject(self, subject_title):
        # Метод на добавление предмета
        # Проверяем, есть ли уже такой предмет
        check_rows = self.__db.execute(
            self.__scripts["check_subject_exists"],
            title=subject_title
        ).fetchall()

        # Если предмет уже есть, вернуть его id
        if check_rows:
            return check_rows[0][0]

        # Получаем максимальный ID в таблице
        max_id_result = self.__db.execute(
            self.__scripts["get_max_id"]).fetchall()
        current_max_id = (
            max_id_result[0][0]
            if max_id_result[0][0] is not None
            else 0
        )

        # Вычисляем новый ID (текущий максимум + 1)
        new_id = current_max_id + 1

        # Создаем новый предмет с явным указанием ID
        self.__db.execute(
            self.__scripts["insert_subject"],
            {"id": new_id, "title": subject_title}
        )

        return new_id

    def get_subject_by_title(self, subject_title):
        # Поиск предмета по названию
        rows = self.__db.execute(
            self.__scripts["select_subject_by_title"],
            {"title": subject_title}
        ).fetchall()
        return rows[0] if rows else None

    def get_subject_by_id(self, subject_id):
        # Поиск предмета по ID
        rows = self.__db.execute(
            self.__scripts["select_subject_by_id"],
            {"id": subject_id}
        ).fetchall()
        return rows[0] if rows else None

    def update_subject_title(self, subject_id, new_title):
        # Обновление названия предмета
        result = self.__db.execute(
            self.__scripts["update_subject"],
            {"new_title": new_title, "id": subject_id}
        )
        return result.rowcount > 0

    def delete_subject(self, subject_id):
        # Удаление предмета
        delete = self.__db.execute(
            self.__scripts["delete_subject"],
            {"id": subject_id}
        )
        return delete.rowcount > 0

    def subject_exists(self, subject_title):
        # Проверка существования предмета
        rows = self.__db.execute(
            self.__scripts["check_subject_exists"],
            {"title": subject_title}
        ).fetchall()
        return len(rows) > 0
