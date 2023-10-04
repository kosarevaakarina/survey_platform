from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from survey.models import Rating
from survey.permissions import IsOwner
from survey.serializers import RatingSerializer


class RatingCreateAPIView(CreateAPIView):
    model = Rating
    permission_classes = [IsAuthenticated]
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()

    def perform_create(self, serializer):
        """При оценке опроса присваивается автор"""
        serializer.save(owner=self.request.user)


class RatingUpdateAPIView(UpdateAPIView):
    model = Rating
    permission_classes = [IsOwner]
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
