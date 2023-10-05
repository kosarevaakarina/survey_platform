from django.urls import path

from survey.views.views_of_answer import AnswerCreateAPIView, AnswerUpdateAPIView
from survey.views.views_of_rating import RatingCreateAPIView
from survey.views.views_of_survey import SurveyListAPIView, SurveyRetrieveAPIView, SurveyCreateAPIView, \
    SurveyUpdateAPIView, SurveyDestroyAPIView, SurveyAndAnswerRetrieveAPIView

from survey.views.views_of_question import QuestionRetrieveAPIView, QuestionCreateAPIView, \
    QuestionUpdateAPIView, QuestionDestroyAPIView

from survey.views.views_of_choice import ChoiceRetrieveAPIView, ChoiceCreateAPIView, \
    ChoiceUpdateAPIView, ChoiceDestroyAPIView

urlpatterns = [
    path('', SurveyListAPIView.as_view(), name='survey_list'),
    path('<int:pk>/', SurveyRetrieveAPIView.as_view(), name='survey_detail'),
    path('create/', SurveyCreateAPIView.as_view(), name='survey_create'),
    path('update/<int:pk>/', SurveyUpdateAPIView.as_view(), name='survey_update'),
    path('delete/<int:pk>/', SurveyDestroyAPIView.as_view(), name='survey_delete'),
    path('question/<int:pk>/', QuestionRetrieveAPIView.as_view(), name='question_detail'),
    path('question/create/', QuestionCreateAPIView.as_view(), name='question_create'),
    path('question/update/<int:pk>/', QuestionUpdateAPIView.as_view(), name='question_update'),
    path('question/delete/<int:pk>/', QuestionDestroyAPIView.as_view(), name='question_delete'),
    path('choice/<int:pk>/', ChoiceRetrieveAPIView.as_view(), name='choice_detail'),
    path('choice/create/', ChoiceCreateAPIView.as_view(), name='choice_create'),
    path('choice/update/<int:pk>/', ChoiceUpdateAPIView.as_view(), name='choice_update'),
    path('choice/delete/<int:pk>/', ChoiceDestroyAPIView.as_view(), name='choice_delete'),
    path('answer/create/', AnswerCreateAPIView.as_view(), name='answer_create'),
    path('answer/update/<int:pk>/', AnswerUpdateAPIView.as_view(), name='answer_update'),
    path('survey/answer/<int:pk>/', SurveyAndAnswerRetrieveAPIView.as_view(), name='survey_answer'),
    path('rating/create/', RatingCreateAPIView.as_view(), name='rating_create'),
]
