from django.urls import path

from survey.views.views_of_survey import SurveyListAPIView, SurveyRetrieveAPIView, SurveyCreateAPIView, \
    SurveyUpdateAPIView, SurveyDestroyAPIView

from survey.views.views_of_question import QuestionListAPIView, QuestionRetrieveAPIView, QuestionCreateAPIView, \
    QuestionUpdateAPIView, QuestionDestroyAPIView

from survey.views.views_of_choice import ChoiceListAPIView, ChoiceRetrieveAPIView, ChoiceCreateAPIView, \
    ChoiceUpdateAPIView, ChoiceDestroyAPIView

urlpatterns = [
    path('', SurveyListAPIView.as_view(), name='survey_list'),
    path('<int:pk>/', SurveyRetrieveAPIView.as_view(), name='survey_detail'),
    path('create/', SurveyCreateAPIView.as_view(), name='survey_create'),
    path('update/<int:pk>/', SurveyUpdateAPIView.as_view(), name='survey_update'),
    path('delete/<int:pk>/', SurveyDestroyAPIView.as_view(), name='survey_delete'),
    path('question/', QuestionListAPIView.as_view(), name='question_list'),
    path('question/<int:pk>', QuestionRetrieveAPIView.as_view(), name='question_detail'),
    path('question/create/', QuestionCreateAPIView.as_view(), name='question_create'),
    path('question/update/<int:pk>/', QuestionUpdateAPIView.as_view(), name='question_update'),
    path('question/delete/<int:pk>/', QuestionDestroyAPIView.as_view(), name='question_delete'),
    path('choice/', ChoiceListAPIView.as_view(), name='choice_list'),
    path('choice/<int:pk>/', ChoiceRetrieveAPIView.as_view(), name='choice_detail'),
    path('choice/create/', ChoiceCreateAPIView.as_view(), name='choice_create'),
    path('choice/update/<int:pk>/', ChoiceUpdateAPIView.as_view(), name='choice_update'),
    path('choice/delete/<int:pk>/', ChoiceDestroyAPIView.as_view(), name='choice_delete'),

]
