from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from survey.models import Survey, CheckSurvey
from survey.permissions import IsOwner
from survey.serializers import SurveySerializer, SurveyListSerializer, SurveyAndAnswerQuestion


class SurveyListAPIView(ListAPIView):
    """Представление для просмотра всех опросов"""
    model = Survey
    serializer_class = SurveyListSerializer
    queryset = Survey.objects.filter(is_published=True)
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        """Сортировка списка опросов по количеству лайков"""
        data = self.serializer_class(self.get_queryset(), many=True).data
        data = sorted(data, key=lambda x: -x['like'])
        return Response(data)


class SurveyRetrieveAPIView(RetrieveAPIView):
    """Представление для просмотра одного опроса"""
    model = Survey
    serializer_class = SurveySerializer
    queryset = Survey.objects.filter(is_published=True)
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """Фиксация просмотра пользователем опроса: при просмотре опроса создается экземпляр класса CheckSurvey"""
        survey = Survey.objects.get(pk=kwargs['pk'])
        if not CheckSurvey.objects.filter(user=request.user, survey=survey).exists():
            CheckSurvey.objects.create(user=request.user, survey=survey)
        return self.retrieve(request, *args, **kwargs)


class SurveyCreateAPIView(CreateAPIView):
    """Представление для создания опроса"""
    model = Survey
    serializer_class = SurveySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """При создании опроса присваивается автор"""
        serializer.save(owner=self.request.user)


class SurveyUpdateAPIView(UpdateAPIView):
    """"Представление для обновления информации об опросе"""
    model = Survey
    serializer_class = SurveySerializer
    queryset = Survey.objects.filter(is_published=True)

    permission_classes = [IsOwner]


class SurveyDestroyAPIView(DestroyAPIView):
    """Представление для удаления опроса"""
    model = Survey
    serializer_class = SurveySerializer
    queryset = Survey.objects.filter(is_published=True)
    permission_classes = [IsOwner]


class SurveyAndAnswerRetrieveAPIView(RetrieveAPIView):
    """Представление для просмотра опроса с ответами"""
    model = Survey
    serializer_class = SurveyAndAnswerQuestion
    permission_classes = [IsAuthenticated]
    queryset = Survey.objects.filter(is_published=True)
