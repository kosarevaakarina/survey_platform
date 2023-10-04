import logging

from django.conf import settings
from django.core.mail import send_mail

from survey.models import Survey
from users.models import User

logger = logging.getLogger("base")


class SendMessage:
    """Сервис по отправке сообщений зарегистрированным пользователям"""

    def __init__(self, survey_id: int):
        self.survey_id = survey_id

    @staticmethod
    def get_users() -> list:
        """Возвращает список пользователей (email)"""
        users = User.objects.all()
        users_email_list = [user.email for user in users]
        return users_email_list

    def get_survey(self) -> tuple:
        """Возвращает название и описание опроса"""
        survey = Survey.objects.get(pk=self.survey_id)
        return survey.title, survey.description

    def get_message(self) -> str:
        """Формирует сообщение для отправки пользователю"""
        title, description = self.get_survey()
        message = f'Добавлен опрос {title}. Описание рассылки: {description}'
        return message

    def send_email(self) -> None:
        """Отправка сообщения пользователям"""
        message = self.get_message()
        users = self.get_users()
        for user in users:
            try:
                send_mail(
                    subject='Добавлен опрос',
                    message=message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[user]
                )
                logger.info(f"Сообщение о создании нового опроса пользователю {user} отправлено")
            except Exception:
                logger.error(f"Сообщение о создании нового опроса пользователю {user} не отправлено")
                raise 'Сообщение не отправлено'
