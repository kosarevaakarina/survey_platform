from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from survey.models import Answer
from survey.serializers import AnswerSerializer


class AnswerCreateAPIView(CreateAPIView):
    """Представление для создания ответа на вопрос"""
    model = Answer
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
    queryset = Answer.objects.all()

    def perform_create(self, serializer):
        """При создании ответа присваивается автор"""
        serializer.save(user=self.request.user)


class AnswerUpdateAPIView(UpdateAPIView):
    model = Answer
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
    queryset = Answer.objects.all()

