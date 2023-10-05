from rest_framework import status

from survey.models import Question
from users.tests.create_user import UserCreate


class AnswerCreateAPITestCase(UserCreate):
    """Тестирование создания ответа на вопрос"""

    def create_response(self):
        """Получение ответа при отправке POST запроса"""
        response = self.client.post('/survey/answer/create/', {
            "question": self.question.pk,
            "answer": self.choice.pk
        })
        return response

    def create_second_response(self):
        self.new_question = Question.objects.create(
            question='Two question',
            survey=self.survey
        )
        response = self.client.post('/survey/answer/create/', {
            "question": self.new_question.pk,
            "answer": self.choice.pk
        })
        return response

    def test_create_answer_unauth_user(self):
        """Тестирование создания ответа неавторизованным пользователем"""
        response = self.create_response()
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {'detail': 'Учетные данные не были предоставлены.'})

    def test_create_answer_auth_user(self):
        """Тестирование создания ответа авторизованным пользователем"""
        self.save_owner_for_answer()
        response = self.create_second_response()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class AnswerUpdateAPITestCase(UserCreate):
    """Тестирование обновления ответа на вопрос"""

    def update_response(self, pk):
        """Получение ответа при отправке PATCH запроса"""
        self.second_question = Question.objects.create(
            question='Second question',
            survey=self.survey
        )
        response = self.client.patch(f'/survey/answer/update/{pk}/', {'question': self.second_question.pk})
        return response

    def test_update_answer_unauth_user(self):
        """Тестирование обновления ответа на вопрос для неавторизованного пользователя"""
        response = self.update_response(self.answer.pk)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {'detail': 'Учетные данные не были предоставлены.'})

    def test_update_answer_auth_user(self):
        """Тестирование обновления ответа на вопрос для авторизованного пользователя"""
        self.save_owner_for_answer()
        response = self.update_response(self.answer.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('question'), self.second_question.pk)
