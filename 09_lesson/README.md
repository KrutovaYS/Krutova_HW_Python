Инструкция для наставника.

Необходимо следовать по шагам:
1. Установить зависимости(если уже установлены - пропустите этот шаг). 
Введите команду в терминале:
pip install pytest sqlalchemy psycopg2-binary python-dotenv

2. Создайте файл .env в папке 09_lesson. Добавьте в файл gitignore - .env(создайте gitignore, если нет)
В графе DB_PASSWORD необходимо ввести свой пароль.
Формат содержимого файла:

DB_USER=postgres
DB_PASSWORD=ваш_пароль
DB_NAME=QAlesson
DB_HOST=localhost
DB_PORT=5432

Примечание: При создании БД на своем локальном компьютере, необходимо ее назвать как указано здесь - QAlesson.
Для создания таблицы используйте SQL:

CREATE TABLE subject (
    subject_id SERIAL PRIMARY KEY,
    subject_title VARCHAR(200) NOT NULL UNIQUE
);

3. Проверьте структуру таблицы subject в базе данных. Должны присутствовать столбцы: subject_id и subject_title

4. Запустите тесты командой в терминале:

pytest test_bd_QAlesson.py -v

ВАЖНО!
При составлении тестов использовалась версия SQLAlchemy 1.4.50. Поэтому при прогоне тестов терминал выдает предупреждение:
RemovedIn20Warning: Deprecated API features detected! These feature(s) are not compatible with SQLAlchemy 2.0.

Данное предупреждение не мешает исполнению тестов.
