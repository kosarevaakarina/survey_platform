from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Пользователь может изменять и удалять только свой опрос"""

    def has_permission(self, request, view):
        return request.user == view.get_object().owner


class IsQuestionOwner(permissions.BasePermission):
    """Пользователь может изменять и удалять только свой вопрос"""

    def has_permission(self, request, view):
        return request.user == view.get_object().survey.owner


class IsChoiceOwner(permissions.BasePermission):
    """Пользователь может изменять и удалять только свой вариант ответа"""

    def has_permission(self, request, view):
        return request.user == view.get_object().question.survey.owner


class IsAnswerOwner(permissions.BasePermission):
    """Пользователь может изменять только свой ответ"""

    def has_permission(self, request, view):
        return request.user == view.get_object().user
