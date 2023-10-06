from rest_framework import status

from users.tests.create_user import UserCreate


class UserPanelAPITestCase(UserCreate):

    def test_retrieve_user_create_survey(self):
        self.save_owner_for_survey()
        response = self.client.get(f'/users/survey/{self.user.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            'email': 'example@test.ru',
            'survey': [{
                'title': 'Test survey',
                'description': 'Test survey description',
                'owner': self.user.pk,
                'num_of_views': 0,
                'like': 0,
                'dislike': 0}]})

    def test_retrieve_user_create_rating(self):
        self.save_owner_for_survey()
        response = self.client.get(f'/users/rating/{self.user.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_user_check_survey(self):
        self.save_owner_for_survey()
        response = self.client.get(f'/users/check/{self.user.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_user_correct_answer_percent(self):
        self.save_owner_for_survey()
        response = self.client.get(f'/users/correct_answer_percent/{self.user.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
