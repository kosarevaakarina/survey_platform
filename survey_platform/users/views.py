from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from users.models import User
from users.permissions import IsUser
from users.serializers import UserRegisterSerializer, UserSerializer, UserCreateSurveySerializer, \
    UserCreateRatingSerializer, UserCheckSurveySerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Представление для регистрации пользователя"""
    model = User
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]


class UserListAPIView(generics.ListAPIView):
    """Представления для просмотра списка пользователей"""
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Представление для просмотра одного пользователя"""
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsUser]


class UserUpdateAPIView(generics.UpdateAPIView):
    """Представление для обновления пользователя"""
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsUser]


class UserDestroyAPIView(generics.DestroyAPIView):
    """Представление для удаления пользователя"""
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsUser]


class UserCreateSurveyListAPIView(generics.ListAPIView):
    """Представление для просмотра созданных пользователем опросов"""
    model = User
    serializer_class = UserCreateSurveySerializer
    permission_classes = [IsUser]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return User.objects.all()
        else:
            return User.objects.filter(pk=user.pk)


class UserCreateRatingListAPIView(generics.ListAPIView):
    """Представление для просмотра проставленных оценок опросам"""
    model = User
    serializer_class = UserCreateRatingSerializer
    permission_classes = [IsUser]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return User.objects.all()
        else:
            return User.objects.filter(pk=user.pk)


class UserCheckSurveyListAPIView(generics.ListAPIView):
    """Представление для списка просмотренных пользователем опросов"""
    model = User
    serializer_class = UserCheckSurveySerializer
    permission_classes = [IsUser]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return User.objects.all()
        else:
            return User.objects.filter(pk=user.pk)
