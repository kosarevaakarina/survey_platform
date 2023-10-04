from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from survey.models import Question
from survey.permissions import IsQuestionOwner
from survey.serializers import QuestionSerializer


class QuestionRetrieveAPIView(RetrieveAPIView):
    """Представление для просмотра одного вопроса"""
    model = Question
    serializer_class = QuestionSerializer
    queryset = Question.objects.filter(is_published=True)
    permission_classes = [IsAuthenticated]


class QuestionCreateAPIView(CreateAPIView):
    """Представление для создания вопроса"""
    model = Question
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]


class QuestionUpdateAPIView(UpdateAPIView):
    """Представления для обновления вопроса"""
    model = Question
    serializer_class = QuestionSerializer
    queryset = Question.objects.filter(is_published=True)
    permission_classes = [IsQuestionOwner]


class QuestionDestroyAPIView(DestroyAPIView):
    """Представление для удаления вопроса"""
    model = Question
    serializer_class = QuestionSerializer
    queryset = Question.objects.filter(is_published=True)
    permission_classes = [IsQuestionOwner]
