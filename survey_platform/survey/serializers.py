from rest_framework import serializers
from survey.models import Survey, Question, Choice, Answer, Rating, CheckSurvey


class ChoiceSerializer(serializers.ModelSerializer):
    """Сериализатор для представления модели выбора ответа"""

    class Meta:
        model = Choice
        fields = '__all__'

    def create(self, validated_data):
        question = validated_data.get('question')
        choice = validated_data.get('choice')
        choices = Choice.objects.filter(question=question)
        if choices.count() >= 4:
            raise serializers.ValidationError(f'Количество ответов на один и тот же вопрос не может быть больше 4!')
        if Choice.objects.filter(question=question, choice=choice).exists():
            raise serializers.ValidationError('Такой вариант ответа для этого вопроса уже существует!')
        return super().create(validated_data)

    def update(self, instance, validated_data):
        question = validated_data.get('question') if validated_data.get('question') is not None else instance.question
        choice = validated_data.get('choice') if validated_data.get('choice') is not None else instance.choice
        if Choice.objects.filter(question=question, choice=choice).exists():
            raise serializers.ValidationError('Такой вариант ответа для этого вопроса уже существует!')
        return super().update(instance, validated_data)


class QuestionSerializer(serializers.ModelSerializer):
    """Сериализатор для представления модели вопроса"""
    choices = ChoiceSerializer(many=True, read_only=True, source='choice_set')

    class Meta:
        model = Question
        fields = ('id', 'question', 'survey', 'choices')

    def create(self, validated_data):
        """При создании вопроса проверяется количество вопросов в данном опросе"""
        survey = validated_data.get('survey')
        question = Question.objects.filter(survey=survey)
        if question.count() > 10:
            raise serializers.ValidationError(f'Количество вопросов в опросе не может быть больше 10!')
        return super().create(validated_data)

    def validate(self, attrs):
        """Валидация повторяющихся вопросов в опросе"""
        survey = attrs.get('survey')
        question = attrs.get('question')
        if Question.objects.filter(survey=survey, question=question).exists():
            raise serializers.ValidationError(f'Вопрос {question} в этом опросе уже существует!')
        return attrs

    def update(self, instance, validated_data):
        """При обновлении вопроса проверяется наличие такого вопроса у этого опроса"""
        survey = validated_data.get('survey') if validated_data.get('survey') is not None else instance.survey
        question = validated_data.get('question') if validated_data.get('question') is not None else instance.question
        if Question.objects.filter(survey=survey, question=question).exists():
            raise serializers.ValidationError(f'Вопрос {question} в этом опросе уже существует!')
        return super().update(instance, validated_data)


class SurveySerializer(serializers.ModelSerializer):
    """"Сериализатор для представления модели опроса"""
    questions = QuestionSerializer(many=True, read_only=True, source='question_set')

    class Meta:
        model = Survey
        fields = ('id', 'create_at', 'title', 'description', 'owner', 'is_published', 'questions')

    def create(self, validated_data):
        """При создании опроса проверяется наличие опросов с таким же названием и описанием"""
        title = validated_data.get('title')
        description = validated_data.get('description')
        if Survey.objects.filter(title=title, description=description).exists():
            raise serializers.ValidationError(f'Опрос {title} с описанием {description} уже существует!')
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """При обновлении опроса проверяется наличие опросов с таким же названием и описанием"""
        title = validated_data.get('title') if validated_data.get('title') is not None else instance.title
        description = validated_data.get('description') if validated_data.get(
            'description') is not None else instance.description
        if Survey.objects.filter(title=title, description=description).exists():
            raise serializers.ValidationError(f'Опрос {title} с описанием {description} уже существует!')
        return super().update(instance, validated_data)


class SurveyListSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра списка опросов"""
    num_of_views = serializers.SerializerMethodField()
    like = serializers.SerializerMethodField()
    dislike = serializers.SerializerMethodField()

    class Meta:
        model = Survey
        fields = ('title', 'description', 'owner', 'num_of_views', 'like', 'dislike')

    @staticmethod
    def get_num_of_views(obj):
        """Расчет количества просмотров опроса"""
        check_survey = CheckSurvey.objects.filter(survey=obj).count()
        return check_survey

    @staticmethod
    def get_like(obj):
        """Расчет количества лайков"""
        like = Rating.objects.filter(survey=obj, like=1).count()
        return like

    @staticmethod
    def get_dislike(obj):
        """Расчет количества дизлайков"""
        dislike = Rating.objects.filter(survey=obj, dislike=1).count()
        return dislike


class AnswerSerializer(serializers.ModelSerializer):
    """Сериализатор для представления ответов на вопросы"""

    class Meta:
        model = Answer
        fields = ('question', 'answer')

    def create(self, validated_data):
        question = validated_data.get('question')
        if Answer.objects.filter(question=question).exists():
            raise serializers.ValidationError('Ответ на этот вопрос уже существует! Вы можете его изменить')
        return super().create(validated_data)

    def update(self, instance, validated_data):
        question = validated_data.get('question') if validated_data.get('question') is not None else instance.question
        if Answer.objects.filter(question=question).exists():
            raise serializers.ValidationError('Ответ на этот вопрос уже существует! Вы можете его изменить')
        return super().update(instance, validated_data)


class QuestionAndAnswerSerializer(serializers.ModelSerializer):
    """Сериализатор для представления информации о вопросах и ответах на них"""
    answer = AnswerSerializer(many=True, read_only=True, source='answer_set')

    class Meta:
        model = Question
        fields = ('question', 'survey', 'answer')


class SurveyAndAnswerQuestion(serializers.ModelSerializer):
    """Сериализатор для представления ответов на вопросы конкретного опроса"""
    question_and_answer = QuestionAndAnswerSerializer(many=True, read_only=True, source='question_set')

    class Meta:
        model = Survey
        fields = ('title', 'description', 'owner', 'question_and_answer')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('survey', 'owner', 'like', 'dislike')

    def validate(self, attrs):
        owner = attrs.get('owner')
        survey = attrs.get('survey')
        like = attrs.get('like')
        dislike = attrs.get('dislike')
        if Rating.objects.filter(owner=owner, survey=survey).exists():
            raise serializers.ValidationError('Вы уже оценивали этот опрос! Вы можете изменить оценку')
        if like is not None and dislike is not None:
            raise serializers.ValidationError('Нельзя одновременно ставить лайк и дизлайк')
        return attrs


