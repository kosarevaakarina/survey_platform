import logging
from rest_framework import serializers
from survey.models import Survey, Question, Choice, Answer, Rating, CheckSurvey
from survey.sevices.send_email_when_create_survey import SendMessage
from survey.sevices.send_mail_when_rating_survey import SendMail

logger = logging.getLogger("base")


class ChoiceSerializer(serializers.ModelSerializer):
    """Сериализатор для представления модели выбора ответа"""

    class Meta:
        model = Choice
        fields = '__all__'

    def create(self, validated_data):
        question = validated_data.get('question')
        choice = validated_data.get('choice')
        choice_count = Choice.objects.filter(question=question).count()
        if choice_count >= 4:
            raise serializers.ValidationError('Количество ответов на один и тот же вопрос не может быть больше 4!')

        logger.info(f"Добавлен вариант ответа {choice} к вопросу {question.question} (ID={question.pk})")

        return super().create(validated_data)

    def validate(self, attrs):
        question = attrs.get('question')
        choice = attrs.get('choice')
        if Choice.objects.filter(question=question, choice=choice).exists():
            raise serializers.ValidationError('Такой вариант ответа для этого вопроса уже существует!')
        return attrs

    def update(self, instance, validated_data):
        question = validated_data.get('question') if validated_data.get('question') is not None else instance.question
        choice = validated_data.get('choice') if validated_data.get('choice') is not None else instance.choice

        logger.info(f"Обновлен вариант ответа {choice} к вопросу {question.question} (ID={question.pk})")

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
        question = validated_data.get('question')
        question_count = Question.objects.filter(survey=survey, is_published=True).count()
        if question_count > 10:
            raise serializers.ValidationError('Количество вопросов в опросе не может быть больше 10!')
        if Question.objects.filter(survey=survey, question=question, is_published=True).exists():
            raise serializers.ValidationError(f'Вопрос {question} в этом опросе уже существует!')

        logger.info(f"Добавлен вопрос {question} к опросу {survey.title} (ID={survey.pk})")

        return super().create(validated_data)

    def update(self, instance, validated_data):
        """При обновлении вопроса проверяется наличие такого вопроса у этого опроса"""
        survey = validated_data.get('survey') if validated_data.get('survey') is not None else instance.survey
        question = validated_data.get('question') if validated_data.get('question') is not None else instance.question
        if Question.objects.filter(survey=survey, question=question, is_published=True).exists():
            raise serializers.ValidationError(f'Вопрос {question} в этом опросе уже существует!')

        logger.info(f"Обновлен вопрос {question} к опросу {survey.title} (ID={survey.pk})")

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
        if Survey.objects.filter(title=title, description=description, is_published=True).exists():
            raise serializers.ValidationError(f'Опрос {title} с описанием {description} уже существует!')
        survey = super().create(validated_data)

        logger.info(f"Добавлен опрос {title}")

        # при создании опроса осуществляется рассылка всем пользователям
        send_mail = SendMessage(survey.id)
        send_mail.send_email()

        return survey

    def update(self, instance, validated_data):
        """При обновлении опроса проверяется наличие опросов с таким же названием и описанием"""
        title = validated_data.get('title') if validated_data.get('title') is not None else instance.title
        description = validated_data.get('description') if validated_data.get(
            'description') is not None else instance.description
        if Survey.objects.filter(title=title, description=description, is_published=True).exists():
            raise serializers.ValidationError(f'Опрос {title} с описанием {description} уже существует!')

        logger.info(f"Обновлен опрос {title} (ID={instance.pk})")

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
        answer = validated_data.get('answer')

        logger.info(f"Добавлен ответ {answer.choice} к вопросу {question.question} (ID={question.pk})")

        return super().create(validated_data)

    def update(self, instance, validated_data):
        question = validated_data.get('question') if validated_data.get('question') is not None else instance.question
        answer = validated_data.get('answer') if validated_data.get('answer') is not None else instance.answer

        logger.info(f"Обновлен ответ {answer.choice} к вопросу {question.question} (ID={question.pk})")

        return super().update(instance, validated_data)


class QuestionAndCorrectChoiceSerializer(serializers.ModelSerializer):
    """Сериализатор для представления информации о вопросах и правильных ответов на них"""
    answer = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ('question', 'answer')

    @staticmethod
    def get_answer(obj):
        answer = Choice.objects.filter(question=obj, points=True)
        if answer.exists():
            return answer.first().choice
        return None


class SurveyAndAnswerQuestion(serializers.ModelSerializer):
    """Сериализатор для представления правильных ответов на вопросы конкретного опроса"""
    answer = QuestionAndCorrectChoiceSerializer(many=True, read_only=True, source='question_set')

    class Meta:
        model = Survey
        fields = ('title', 'description', 'owner', 'answer')


class RatingSerializer(serializers.ModelSerializer):
    """Сериализатор для представления оценки опроса"""

    class Meta:
        model = Rating
        fields = ('survey', 'owner', 'like', 'dislike')

    def validate(self, attrs):
        like = attrs.get('like')
        dislike = attrs.get('dislike')
        # проверка, что поставлен лайк или дизлайк
        if like is True and dislike is True:
            raise serializers.ValidationError('Нельзя одновременно ставить лайк и дизлайк')
        # проверка, что не поставлены одновременно лайк и дизлайк
        if like is False and dislike is False:
            raise serializers.ValidationError('Необходимо поставить или лайк, или дизлайк')

        return attrs

    def create(self, validated_data):
        # проверка, что лайк и дизлайк не поставлен повторно
        if Rating.objects.filter(owner=validated_data.get('owner'), survey=validated_data.get('survey')).exists():
            raise serializers.ValidationError('Вы уже оценивали этот опрос! Вы можете изменить оценку')

        rating = super().create(validated_data)

        # при создании новой оценки опроса формируется и отправляется сообщение автору опроса
        send_message = SendMail(rating.id)
        send_message.send_email()

        logger.info(f"Пользователь {rating.owner} поставил оценку вопросу {rating.survey.title}")

        return rating
