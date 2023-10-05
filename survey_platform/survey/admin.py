from django.contrib import admin

from survey.models import Survey, Question, Choice, Answer


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    """Административная панель для модели Survey"""
    list_display = ('title', 'create_at')
    fieldsets = (
        (None, {'fields': ('title',)}),
        ('Описание', {'fields': ('description',)}),
        ('Автор', {'fields': ('owner',)}),
        ('Публикация', {'fields': ('is_published',)}),
    )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Административная панель для модели Question"""
    list_display = ('survey', 'question')
    fieldsets = (
        (None, {'fields': ('question',)}),
        ('Опрос', {'fields': ('survey',)}),
        ('Публикация', {'fields': ('is_published',)}),
    )


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    """Административная панель для модели Choice"""
    list_display = ('question', 'choice')
    fieldsets = (
        ('Вопрос', {'fields': ('question',)}),
        ('Вариант ответа', {'fields': ('choice',)}),
    )


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    """Административная панель для модели Answer"""
    list_display = ('question', 'answer')
    fieldsets = (
        ('Вопрос', {'fields': ('question',)}),
        ('Ответ', {'fields': ('answer',)}),
        ('Автор', {'fields': ('user',)}),
    )
