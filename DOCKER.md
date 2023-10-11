_Для работы с переменными окружениями необходимо создать файл .env и заполнить его согласно файлу .env.example:_
```
# Secret_key
SECRET_KEY=

# Database
POSTGRES_ENGINE='django.db.backends.postgresql'
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST='db'
POSTGRES_PORT=5432
POSTGRES_HOST_AUTH_METHOD=trust

#Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=

#Email
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=

```
_Для создания образа из Dockerfile и запуска контейнера запустить команду:_
```
docker-compose up --build
```
_или_
```
docker-compose up -d --build
```
_Второй вариант для запуска в фоновом режиме._

_Для тестирования проекта запустить команду:_

```
docker-compose exec app python3 manage.py test
```