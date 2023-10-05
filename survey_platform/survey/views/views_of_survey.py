from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from survey.models import Survey
from survey.serializers import SurveySerializer


class SurveyListAPIView(ListAPIView):
    model = Survey
    serializer_class = SurveySerializer
    queryset = Survey.objects.filter(is_published=True)


class SurveyRetrieveAPIView(RetrieveAPIView):
    model = Survey
    serializer_class = SurveySerializer
    queryset = Survey.objects.filter(is_published=True)


class SurveyCreateAPIView(CreateAPIView):
    model = Survey
    serializer_class = SurveySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SurveyUpdateAPIView(UpdateAPIView):
    model = Survey
    serializer_class = SurveySerializer


class SurveyDestroyAPIView(DestroyAPIView):
    model = Survey
    serializer_class = SurveySerializer
