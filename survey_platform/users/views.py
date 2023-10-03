from rest_framework import generics

from users.models import User
from users.serializers import UserRegisterSerializer, UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Представление для регистрации пользователя"""
    model = User
    serializer_class = UserRegisterSerializer


class UserListAPIView(generics.ListAPIView):
    """Представления для просмотра списка пользователей"""
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Представление для просмотра одного пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    """Представление для обновления пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    """Представление для удаления пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
