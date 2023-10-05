from rest_framework import status

from users.tests.create_user import UserCreate


class ChoiceCreateAPITestCase(UserCreate):
    """Тестирование создания варианта ответа"""

    def create_response(self):
        """Получение ответа при отправке POST запроса"""
        response = self.client.post('/choice/create/', {
            "question": self.question.pk,
            "choice": "Choice answer"
        })
        return response

    def test_create_choice_unauth_user(self):
        """Тестирование создания варианта ответа неавторизованным пользователем"""
        response = self.create_response()
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {'detail': 'Учетные данные не были предоставлены.'})

    def test_create_choice_auth_user(self):
        """Тестирование создания варианта ответа авторизованным пользователем"""
        self.save_owner_for_survey()
        response = self.create_response()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ChoiceRetrieveAPITestCase(UserCreate):
    """Тестирование просмотра одного варианта ответа"""

    def retrieve_response(self, pk):
        """Получение ответа при отправке GET запроса"""
        response = self.client.get(f'/choice/{pk}/')
        return response

    def test_retrieve_choice_unauth_user(self):
        """Тестирование просмотра одного варианта ответа для неавторизованного пользователя"""
        response = self.retrieve_response(self.choice.pk)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {'detail': 'Учетные данные не были предоставлены.'})

    def test_retrieve_choice_auth_user(self):
        """Тестирование просмотра одного варианта ответа для авторизованного пользователя"""
        self.save_owner_for_survey()
        response = self.retrieve_response(self.choice.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            'id': self.choice.pk,
            'choice': 'Test choice',
            'points': True,
            'question': self.question.pk})


class ChoiceUpdateAPITestCase(UserCreate):
    """Тестирование обновления варианта ответа"""
    def update_response(self, pk):
        """Получение ответа при отправке PATCH запроса"""
        response = self.client.patch(f'/choice/update/{pk}/', {'choice': 'Update choice'})
        return response

    def test_update_choice_unauth_user(self):
        """Тестирование обновления варианта ответа для неавторизованного пользователя"""
        response = self.update_response(self.choice.pk)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {'detail': 'Учетные данные не были предоставлены.'})

    def test_update_choice_auth_user(self):
        """Тестирование обновления варианта ответа для авторизованного пользователя"""
        self.save_owner_for_survey()
        response = self.update_response(self.choice.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('choice'), 'Update choice')


class ChoiceDeleteAPITestCase(UserCreate):
    """Тестирование удаления варианта ответа"""
    def delete_response(self, pk):
        """Получение ответа при отправке DELETE запроса"""
        response = self.client.delete(f'/choice/delete/{pk}/')
        return response

    def test_delete_choice_unauth_user(self):
        """Тестирование удаления варианта ответа неавторизованным пользователем"""
        response = self.delete_response(self.choice.pk)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {'detail': 'Учетные данные не были предоставлены.'})

    def test_delete_choice_auth_user(self):
        """Тестирование удаления варианта ответа авторизованным пользователем"""
        self.save_owner_for_survey()
        response = self.delete_response(self.choice.pk)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)