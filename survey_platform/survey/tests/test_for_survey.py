from rest_framework import status

from users.tests.create_user import UserCreate


class SurveyCreateAPITestCase(UserCreate):
    """Тестирование создания опроса"""

    def create_response(self):
        """Получение ответа при отправке POST запроса"""
        response = self.client.post('/create/', {
            "title": "Test title survey",
            "description": "Test description survey"
        })
        return response

    def test_create_survey_unauth_user(self):
        """Тестирование создания опроса неавторизованным пользователем"""
        response = self.create_response()
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {'detail': 'Учетные данные не были предоставлены.'})

    def test_create_survey_auth_user(self):
        """Тестирование создания опроса авторизованным пользователем"""
        self.save_owner_for_survey()
        response = self.create_response()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class SurveyListAPITestCase(UserCreate):
    """Тестирование просмотра опросов"""
    def get_response(self):
        """Получение ответа при отправке GET запроса"""
        response = self.client.get('', )
        return response

    def test_get_survey_unauth_user(self):
        """Тестирование просмотра опросов неавторизованным пользователем"""
        response = self.get_response()
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {'detail': 'Учетные данные не были предоставлены.'})

    def test_get_survey_auth_user(self):
        """Тестирование просмотра опросов авторизованным пользователем"""
        self.save_owner_for_survey()
        response = self.get_response()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [{
            'title': 'Test survey',
            'description': 'Test survey description',
            'owner': self.user.pk,
            'num_of_views': 0,
            'like': 0,
            'dislike': 0}])


class SurveyRetrieveAPITestCase(UserCreate):
    """Тестирование просмотра одного опроса"""

    def retrieve_response(self, pk):
        """Получение ответа при отправке GET запроса"""
        response = self.client.get(f'/{pk}/')
        return response

    def test_retrieve_survey_unauth_user(self):
        """Тестирование просмотра одного опроса для неавторизованного пользователя"""
        response = self.retrieve_response(self.survey.pk)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {'detail': 'Учетные данные не были предоставлены.'})

    def test_retrieve_survey_auth_user(self):
        """Тестирование просмотра одного опроса для авторизованного пользователя"""
        self.save_owner_for_survey()
        response = self.retrieve_response(self.survey.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SurveyUpdateAPITestCase(UserCreate):
    """Тестирование обновления опроса"""
    def update_response(self, pk):
        """Получение ответа при отправке PATCH запроса"""
        response = self.client.patch(f'/update/{pk}/', {'title': 'Update title'})
        return response

    def test_update_survey_unauth_user(self):
        """Тестирование обновления опроса для неавторизованного пользователя"""
        response = self.update_response(self.survey.pk)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {'detail': 'Учетные данные не были предоставлены.'})

    def test_update_survey_auth_user(self):
        """Тестирование обновления опроса для авторизованного пользователя"""
        self.save_owner_for_survey()
        response = self.update_response(self.survey.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), 'Update title')


class SurveyDeleteAPITestCase(UserCreate):
    """Тестирование удаления опроса"""
    def delete_response(self, pk):
        """Получение ответа при отправке DELETE запроса"""
        response = self.client.delete(f'/delete/{pk}/')
        return response

    def test_delete_survey_unauth_user(self):
        """Тестирование удаления опроса неавторизованным пользователем"""
        response = self.delete_response(self.survey.pk)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {'detail': 'Учетные данные не были предоставлены.'})

    def test_delete_survey_auth_user(self):
        """Тестирование удаления опроса авторизованным пользователем"""
        self.save_owner_for_survey()
        response = self.delete_response(self.survey.pk)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SurveyAndCorrectChoiceRetrieveAPIView(UserCreate):
    def response(self, pk):
        response = self.client.get(f'/survey/answer/{pk}/')
        return response

    def test_get_survey_and_correct_answer(self):
        self.save_owner_for_survey()
        response = self.response(self.survey.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            'title': 'Test survey',
            'description': 'Test survey description',
            'owner': self.user.pk,
            'answer': [{
                'question': 'Test question',
                'answer': 'Test choice'}]})