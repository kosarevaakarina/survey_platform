from django.urls import path
from users.views import UserListAPIView, UserCreateAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView, \
    UserCreateSurveyRetrieveAPIView, UserCreateRatingRetrieveAPIView, UserCheckSurveyRetrieveAPIView

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='user_register'),
    path('', UserListAPIView.as_view(), name='user_list'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user_retrieve'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),
    path('survey/<int:pk>/', UserCreateSurveyRetrieveAPIView.as_view(), name='survey_list'),
    path('rating/<int:pk>/', UserCreateRatingRetrieveAPIView.as_view(), name='rating_list'),
    path('check/<int:pk>/', UserCheckSurveyRetrieveAPIView.as_view(), name='check_list')
]
