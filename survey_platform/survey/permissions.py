from rest_framework import permissions


class IsSurveyOwner (permissions.BasePermission):
    """Пользователь может изменять и удалять только свой опрос"""
    def has_permission(self, request, view):
        return request.user == view.get_object().owner


class IsQuestionOwner (permissions.BasePermission):
    """Пользователь может изменять и удалять только свой опрос"""
    def has_permission(self, request, view):
        return request.user == view.get_object().survey.owner


class IsChoiceOwner (permissions.BasePermission):
    """Пользователь может изменять и удалять только свой опрос"""
    def has_permission(self, request, view):
        return request.user == view.get_object().question.survey.owner

