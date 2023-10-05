from rest_framework import status

from users.tests.create_user import UserCreate


class QuestionCreateAPITestCase(UserCreate):
    """Тестирование создания вопроса"""

    def create_response(self):
        """Получение ответа при отправке POST запроса"""
        response = self.client.post('/survey/question/create/', {
            "question": "Question",
            "survey": self.survey.pk
        })
        return response

    def test_create_question_unauth_user(self):
        """Тестирование создания вопроса неавторизованным пользователем"""
        response = self.create_response()
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {'detail': 'Учетные данные не были предоставлены.'})

    def test_create_question_auth_user(self):
        """Тестирование создания вопроса авторизованным пользователем"""
        self.save_owner_for_survey()
        response = self.create_response()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class QuestionRetrieveAPITestCase(UserCreate):
    """Тестирование просмотра одного вопроса"""

    def retrieve_response(self, pk):
        """Получение ответа при отправке GET запроса"""
        response = self.client.get(f'/survey/question/{pk}/')
        return response

    def test_retrieve_question_unauth_user(self):
        """Тестирование просмотра одного вопроса для неавторизованного пользователя"""
        response = self.retrieve_response(self.question.pk)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {'detail': 'Учетные данные не были предоставлены.'})

    def test_retrieve_question_auth_user(self):
        """Тестирование просмотра одного вопроса для авторизованного пользователя"""
        self.save_owner_for_survey()
        response = self.retrieve_response(self.question.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            'id': self.question.pk,
            'question': 'Test question',
            'survey': self.survey.pk,
            'choices': [
                {'choice': 'Test choice',
                 'id': self.choice.pk,
                 'points': True,
                 'question': self.question.pk}
            ]})


class QuestionUpdateAPITestCase(UserCreate):
    """Тестирование обновления вопроса"""
    def update_response(self, pk):
        """Получение ответа при отправке PATCH запроса"""
        response = self.client.patch(f'/survey/question/update/{pk}/', {'question': 'Update question'})
        return response

    def test_update_question_unauth_user(self):
        """Тестирование обновления вопроса для неавторизованного пользователя"""
        response = self.update_response(self.question.pk)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {'detail': 'Учетные данные не были предоставлены.'})

    def test_update_question_auth_user(self):
        """Тестирование обновления вопроса для авторизованного пользователя"""
        self.save_owner_for_survey()
        response = self.update_response(self.question.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('question'), 'Update question')


class QuestionDeleteAPITestCase(UserCreate):
    """Тестирование удаления вопроса"""
    def delete_response(self, pk):
        """Получение ответа при отправке DELETE запроса"""
        response = self.client.delete(f'/survey/question/delete/{pk}/')
        return response

    def test_delete_question_unauth_user(self):
        """Тестирование удаления вопроса неавторизованным пользователем"""
        response = self.delete_response(self.question.pk)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {'detail': 'Учетные данные не были предоставлены.'})

    def test_delete_question_auth_user(self):
        """Тестирование удаления вопроса авторизованным пользователем"""
        self.save_owner_for_survey()
        response = self.delete_response(self.question.pk)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
