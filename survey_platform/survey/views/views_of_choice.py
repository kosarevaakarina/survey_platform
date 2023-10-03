from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from survey.models import Choice
from survey.serializers import ChoiceSerializer


class ChoiceListAPIView(ListAPIView):
    model = Choice
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()


class ChoiceRetrieveAPIView(RetrieveAPIView):
    model = Choice
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()


class ChoiceCreateAPIView(CreateAPIView):
    model = Choice
    serializer_class = ChoiceSerializer


class ChoiceUpdateAPIView(UpdateAPIView):
    model = Choice
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()


class ChoiceDestroyAPIView(DestroyAPIView):
    model = Choice
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()
