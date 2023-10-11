_Для запуска проекта необходимо клонировать репозиторий и создать и активировать виртуальное окружение:_ 
```
python3 -m venv venv
```
```
source venv/bin/activate
```
_Перейти в рабочую директорию:_
```
cd survey_platform
```
_Установить зависимости:_
```
pip install -r requirements.txt
```
_Для работы с переменными окружениями необходимо создать файл .env и заполнить его согласно файлу .env.sample:_

_Выполнить миграции:_
```
python3 manage.py migrate
```

_Для создания администратора запустить команду:_

```
python3 manage.py createsuperuser
```
_Для добавления тестовых фикстур:_:
```
python3 manage.py loaddata users.json
python3 manage.py loaddata survey.json
```
_Для запуска приложения:_

```
python3 manage.py runserver
```

_Для тестирования проекта необходимо_:
_Запустить команду:_

```
python3 manage.py test
```

_Для запуска подсчета покрытия и вывода отчет запустить команды:_

```
coverage run --source='users,survey' manage.py test

coverage report
```