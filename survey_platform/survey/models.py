from django.conf import settings
from django.db import models

from users.models import NULLABLE


class Survey(models.Model):
    """Модель опроса"""
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания опроса')
    title = models.CharField(max_length=50, verbose_name='название опроса')
    description = models.TextField(verbose_name='описание опроса', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='автор', **NULLABLE)

    is_published = models.BooleanField(default=True, verbose_name='опубликовано')

    class Meta:
        verbose_name = 'опрос'
        verbose_name_plural = 'опросы'

    def __str__(self):
        """Строковое представление модели опроса"""
        return self.title

    def delete(self, using=None, keep_parents=False):
        """При удалении опроса меняется его статус публичности"""
        self.is_published = False
        self.save()


class Question(models.Model):
    """Модель вопроса"""
    question = models.TextField(verbose_name='вопрос')
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name='опрос')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'

    def __str__(self):
        """Строковое представление модели вопроса"""
        return self.question

    def delete(self, using=None, keep_parents=False):
        """При удалении вопроса меняется его статус публичности"""
        self.is_published = False
        self.save()


class Choice(models.Model):
    """Модель варианта ответа"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='вопрос')
    choice = models.CharField(max_length=300, verbose_name='ответ')

    class Meta:
        verbose_name = 'вариант ответа'
        verbose_name_plural = 'варианты ответа'

    def __str__(self):
        return f'{self.question} - {self.choice}'


class Answer(models.Model):
    """Модель ответа"""
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='дата и время ответа')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='автор', **NULLABLE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='вопрос')
    answer = models.ForeignKey(Choice, on_delete=models.CASCADE, verbose_name='ответ')

    class Meta:
        verbose_name = 'ответ'
        verbose_name_plural = 'ответы'

    def __str__(self):
        """Строковое представление модели ответа"""
        return f'{self.answer}'


class CheckSurvey(models.Model):
    """Модель для фиксации просмотра опроса"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='пользователь', on_delete=models.CASCADE, **NULLABLE)
    survey = models.ForeignKey(Survey, verbose_name='опрос', on_delete=models.CASCADE, **NULLABLE)

    class Meta:
        verbose_name = 'просмотр'
        verbose_name_plural = 'просмотры'

    def __str__(self):
        return f'{self.survey} - {self.user}'
