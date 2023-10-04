from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from users.models import User
from users.permissions import IsUser
from users.serializers import UserRegisterSerializer, UserSerializer, UserCreateSurveySerializer, \
    UserCreateRatingSerializer, UserCheckSurveySerializer


class UserCreateAPIView(CreateAPIView):
    """Представление для регистрации пользователя"""
    model = User
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]


class UserListAPIView(ListAPIView):
    """Представления для просмотра списка пользователей"""
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserRetrieveAPIView(RetrieveAPIView):
    """Представление для просмотра одного пользователя"""
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsUser]


class UserUpdateAPIView(UpdateAPIView):
    """Представление для обновления пользователя"""
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsUser]


class UserDestroyAPIView(DestroyAPIView):
    """Представление для удаления пользователя"""
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsUser]


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
