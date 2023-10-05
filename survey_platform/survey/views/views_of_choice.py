from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from survey.models import Choice
from survey.permissions import IsChoiceOwner
from survey.serializers import ChoiceSerializer


class ChoiceRetrieveAPIView(RetrieveAPIView):
    """Представление для просмотра одного варианта ответа"""
    model = Choice
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.filter(question__is_published=True)
    permission_classes = [IsAuthenticated]


class ChoiceCreateAPIView(CreateAPIView):
    """Представление для создания варианта ответа"""
    model = Choice
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.filter(question__is_published=True)
    permission_classes = [IsAuthenticated]


class ChoiceUpdateAPIView(UpdateAPIView):
    """Представление для обновления варианта ответа"""
    model = Choice
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.filter(question__is_published=True)
    permission_classes = [IsChoiceOwner]


class ChoiceDestroyAPIView(DestroyAPIView):
    """Представление для удаления варианта ответа"""
    model = Choice
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.filter(question__is_published=True)
    permission_classes = [IsChoiceOwner]
