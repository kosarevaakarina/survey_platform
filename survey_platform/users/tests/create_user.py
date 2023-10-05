from rest_framework.test import APITestCase

from survey.models import Survey, Question, Choice, Answer
from users.models import User


class UserCreate(APITestCase):
    def setUp(self) -> None:
        self.survey = Survey.objects.create(
            title='Test survey',
            description='Test survey description',
        )
        self.question = Question.objects.create(
            question='Test question',
            survey=self.survey
        )
        self.choice = Choice.objects.create(
            question=self.question,
            choice='Test choice',
            points=True
        )
        self.answer = Answer.objects.create(
            question=self.question,
            answer=self.choice
        )

    def create_user(self):
        """Создание и авторизация пользователя"""
        self.email = 'example@test.ru'
        user_data = {
            'email': self.email,
            'first_name': 'Test',
            'last_name': 'Testov'
        }
        self.user = User(**user_data)
        self.user.set_password('123Qaz')
        self.user.save()
        response = self.client.post(
            '/users/token/',
            {
                'email': self.email,
                'password': '123Qaz'
            }
        )
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def save_owner_for_survey(self):
        """Привязка пользователя к опросу"""
        self.create_user()
        self.survey.owner = self.user
        self.survey.save()

    def save_owner_for_answer(self):
        """Привязка пользователя к ответу"""
        self.create_user()
        self.answer.user = self.user
        self.answer.save()
