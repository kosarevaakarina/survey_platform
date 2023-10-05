from rest_framework import status

from survey.models import Survey
from users.tests.create_user import UserCreate


class RatingCreateAPITestCase(UserCreate):

    def create_new_survey(self):
        self.new_survey = Survey.objects.create(title='Title', description='Description')

    def test_create_rating(self):
        self.create_user()
        self.create_new_survey()
        response = self.client.post('/rating/create/', {
            "survey": self.new_survey.pk,
            "like": True,
            "dislike": False
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {
            'survey': self.new_survey.pk,
            'owner': self.user.pk,
            'like': True,
            'dislike': False})

    def test_create_rating_fatal_one(self):
        self.create_user()
        self.create_new_survey()
        response = self.client.post('/rating/create/', {
            "survey": self.new_survey.pk,
            "like": True,
            "dislike": True
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {'non_field_errors': ['Нельзя одновременно ставить лайк и дизлайк']})

    def test_create_rating_fatal_two(self):
        self.create_user()
        self.create_new_survey()
        response = self.client.post('/rating/create/', {
            "survey": self.new_survey.pk,
            "like": False,
            "dislike": False
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {'non_field_errors': ['Необходимо поставить или лайк, или дизлайк']})
