from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from survey.models import Question
from survey.serializers import QuestionSerializer


class QuestionListAPIView(ListAPIView):
    model = Question
    serializer_class = QuestionSerializer
    queryset = Question.objects.filter(is_published=True)


class QuestionRetrieveAPIView(RetrieveAPIView):
    model = Question
    serializer_class = QuestionSerializer
    queryset = Question.objects.filter(is_published=True)


class QuestionCreateAPIView(CreateAPIView):
    model = Question
    serializer_class = QuestionSerializer


class QuestionUpdateAPIView(UpdateAPIView):
    model = Question
    serializer_class = QuestionSerializer


class QuestionDestroyAPIView(DestroyAPIView):
    model = Question
    serializer_class = QuestionSerializer
