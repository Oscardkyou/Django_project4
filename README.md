

    Python (версия, например, 3.8+)
    pip
    virtualenv (рекомендуется)

Установка

    Клонировать репозиторий:

    bash

git clone [ссылка на ваш репозиторий]
cd [имя вашего проекта или каталога]

(Рекомендуется) Создать и активировать виртуальное окружение:

bash

virtualenv venv
source venv/bin/activate  # на Linux/macOS
venv\Scripts\activate     # на Windows

Установить зависимости:

bash

pip install -r requirements.txt

Применить миграции:

bash

python manage.py migrate

Запустить разработческий сервер:

bash

    python manage.py runserver

Теперь ваш проект должен быть доступен по адресу http://127.0.0.1:8000/.
