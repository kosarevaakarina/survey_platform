from rest_framework.generics import RetrieveAPIView

from users.models import User
from users.permissions import IsUser
from users.serializers import UserCreateSurveySerializer, UserCreateRatingSerializer, UserCheckSurveySerializer, \
    UserPointsSerializer


class UserCreateSurveyRetrieveAPIView(RetrieveAPIView):
    """Представление для просмотра созданных пользователем опросов"""
    model = User
    serializer_class = UserCreateSurveySerializer
    permission_classes = [IsUser]
    queryset = User.objects.all()


class UserCreateRatingRetrieveAPIView(RetrieveAPIView):
    """Представление для просмотра проставленных оценок опросам"""
    model = User
    serializer_class = UserCreateRatingSerializer
    permission_classes = [IsUser]
    queryset = User.objects.all()


class UserCheckSurveyRetrieveAPIView(RetrieveAPIView):
    """Представление для списка просмотренных пользователем опросов"""
    model = User
    serializer_class = UserCheckSurveySerializer
    permission_classes = [IsUser]
    queryset = User.objects.all()


class UserPointsRetrieveAPIView(RetrieveAPIView):
    """Представление для просмотра процентного содержания правильных ответов"""
    model = User
    serializer_class = UserPointsSerializer
    permission_classes = [IsUser]
    queryset = User.objects.all()
