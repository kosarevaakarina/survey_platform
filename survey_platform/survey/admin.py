from django.contrib import admin

from survey.models import Survey, Question, Choice, Answer, CheckSurvey


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    """Административная панель для модели User"""
    list_display = ('title', 'create_at')
    fieldsets = (
        (None, {'fields': ('title',)}),
        ('Описание', {'fields': ('description',)}),
        ('Автор', {'fields': ('owner',)}),
        ('Публикация', {'fields': ('is_published',)}),
    )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('survey', 'question')
    fieldsets = (
        (None, {'fields': ('question',)}),
        ('Опрос', {'fields': ('survey',)}),
        ('Публикация', {'fields': ('is_published',)}),
    )


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice')
    fieldsets = (
        ('Вопрос', {'fields': ('question',)}),
        ('Вариант ответа', {'fields': ('choice',)}),
    )


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    fieldsets = (
        ('Вопрос', {'fields': ('question',)}),
        ('Ответ', {'fields': ('choice',)}),
        ('Автор', {'fields': ('user',)}),

    )


@admin.register(CheckSurvey)
class CheckSurveyAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
