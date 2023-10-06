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
_Для запуска приложения:_

```
python3 manage.py runserver
```

_Для тестирования проекта необходимо_:
В config/settings.py внести изменения, так как при тестировании авторизация осуществляется с помощью JWT:
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'drf_social_oauth2.authentication.SocialAuthentication',
    ),
}
```
_Запустить команду:_

```
python3 manage.py test
```

_Для запуска подсчета покрытия и вывода отчет запустить команды:_

```
coverage run --source='users,survey' manage.py test

coverage report
```