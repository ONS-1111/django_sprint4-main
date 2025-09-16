"""Статичные страницы и обработчики ошибок."""

from django.shortcuts import render
from django.views.generic import TemplateView


class AboutTemplateView(TemplateView):
    """Страница «О проекте/о сайте»."""

    template_name = 'pages/about.html'


class RulesTemplateView(TemplateView):
    """Страница с правилами."""

    template_name = 'pages/rules.html'


def permission_denied(request, exception):
    """Кастомная страница ошибки 403 (не достаточно прав)."""
    return render(request, 'pages/403.html', status=403)


def csrf_failure(request, reason=''):
    """Кастомная страница ошибки 403 CSRF."""
    return render(request, 'pages/403csrf.html', status=403)


def page_not_found(request, exception):
    """Кастомная страница ошибки 404 (не найдено)."""
    return render(request, 'pages/404.html', status=404)


def server_error(request):
    """Кастомная страница ошибки 500 (внутренняя ошибка сервера)."""
    return render(request, 'pages/500.html', status=500)
