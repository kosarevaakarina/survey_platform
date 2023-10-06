import logging
from rest_framework import serializers

from survey.models import CheckSurvey, Answer, Choice
from survey.serializers import SurveyListSerializer, RatingSerializer, AnswerSerializer
from users.models import User

logger = logging.getLogger("base")


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для пользователя"""

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'is_active')

    def update(self, instance, validated_data):
        logger.info(f"Пользователь {instance.email} (ID={instance.pk}) обновил информацию")

        super().update(instance, validated_data)
        return instance


class UserRegisterSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации пользователя"""
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'password2')

    def validate(self, attrs):
        """Валидация паролей"""
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Пароли не совпадают. Проверьте введенные данные")
        return attrs

    def save(self, *args, **kwargs):
        """Метод для сохранения нового пользователя"""
        user = User.objects.create(
            email=self.validated_data.get('email'),
            first_name=self.validated_data.get('first_name'),
            last_name=self.validated_data.get('last_name'),
        )
        # Сохраняем пароль
        password = self.validated_data.get('password')
        user.set_password(password)
        user.save()

        logger.info(f"Пользователь {self.validated_data['email']} зарегистрирован")

        return user


class UserCreateSurveySerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра созданных пользователем опросов"""
    survey = SurveyListSerializer(many=True, read_only=True, source='survey_set')

    class Meta:
        model = User
        fields = ('email', 'survey')


class UserCreateRatingSerializer(serializers.ModelSerializer):
    """Представление для просмотра проставленных оценок пользователем опросам"""
    rating = RatingSerializer(many=True, read_only=True, source='rating_set')

    class Meta:
        model = User
        fields = ('email', 'rating')


class CheckSurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckSurvey
        fields = ('id', 'survey')


class UserCheckSurveySerializer(serializers.ModelSerializer):
    """Сериализатор для списка просмотренных пользователем опросов"""
    check = CheckSurveySerializer(many=True, read_only=True, source='checksurvey_set')

    class Meta:
        model = User
        fields = ('email', 'check')


class UserPointsSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода процента правильных ответов пользователя"""
    percent_correct_answer = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('email', 'percent_correct_answer')

    @staticmethod
    def get_percent_points(obj):
        """Возвращает количество правильных ответов в процентах"""
        answer_count = Answer.objects.filter(user=obj).count()
        correct_choices = Choice.objects.filter(points=True)
        count = 0
        for correct_choice in correct_choices:
            if Answer.objects.filter(answer=correct_choice, user=obj).exists():
                count += 1

        return round(count * 100 / answer_count, 1)
