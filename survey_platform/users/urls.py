from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views.views_of_user_panel import UserCreateSurveyRetrieveAPIView, UserCreateRatingRetrieveAPIView, \
    UserCheckSurveyRetrieveAPIView, UserPointsRetrieveAPIView
from users.views.views_of_users import UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, \
    UserDestroyAPIView

urlpatterns = [
    # users
    path('register/', UserCreateAPIView.as_view(), name='user_register'),
    path('', UserListAPIView.as_view(), name='user_list'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user_retrieve'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),

    # user panel
    path('survey/<int:pk>/', UserCreateSurveyRetrieveAPIView.as_view(), name='survey_list'),
    path('rating/<int:pk>/', UserCreateRatingRetrieveAPIView.as_view(), name='rating_list'),
    path('check/<int:pk>/', UserCheckSurveyRetrieveAPIView.as_view(), name='check_list'),
    path('correct_answer_percent/<int:pk>/', UserPointsRetrieveAPIView.as_view(), name='check_list'),

    # token for test
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
