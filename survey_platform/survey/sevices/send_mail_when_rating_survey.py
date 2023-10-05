import logging

from django.conf import settings
from django.core.mail import send_mail
from survey.models import Rating

logger = logging.getLogger("base")


class SendMail:
    """Сервис по отправке сообщению пользователю при получении новой оценки опроса"""
    def __init__(self, rating_id: int):
        """Инициализация класса"""
        self.rating_id = rating_id
        self.rating = None

    def get_user(self) -> str:
        """Возвращает пользователя-автора опроса"""
        self.rating = Rating.objects.get(pk=self.rating_id)
        user = self.rating.survey.owner
        return user

    def get_message(self) -> str:
        """Формирует сообщение для отправки пользователю"""
        like = self.rating.like
        dislike = self.rating.dislike
        if like is True:
            message = f'Пользователь {self.rating.owner} поставил лайк вашему опросу {self.rating.survey}'
        elif dislike is True:
            message = f'Пользователь {self.rating.owner} поставил дизлайк вашему опросу {self.rating.survey}'

        return message

    def send_email(self) -> None:
        """Отправка сообщения пользователю"""
        user = self.get_user()
        message = self.get_message()
        try:
            send_mail(
                subject='Ваш опрос получил новую оценку',
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user]
            )
            logger.info(f"Сообщение о новой оценке пользователю {user} отправлено")
        except Exception:
            logger.error(f"Сообщение о новой оценке пользователю {user} отправлено")
            raise 'Сообщение не отправлено'
