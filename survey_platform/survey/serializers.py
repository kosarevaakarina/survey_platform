from rest_framework import serializers

from survey.models import Survey, Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    """Сериализатор для представления модели выбора ответа"""
    class Meta:
        model = Choice
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    """Сериализатор для представления модели вопроса"""
    choices = ChoiceSerializer(many=True, read_only=True, source='choice_set')

    class Meta:
        model = Question
        fields = ('id', 'title', 'question', 'survey', 'choices')


class SurveySerializer(serializers.ModelSerializer):
    """"Сериализатор для представления модели опроса"""
    questions = QuestionSerializer(many=True, read_only=True, source='question_set')

    class Meta:
        model = Survey
        fields = ('id', 'create_at', 'title', 'description', 'owner', 'is_published', 'questions')
