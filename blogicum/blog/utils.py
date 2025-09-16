"""Вспомогательные утилиты для фильтрации queryset-ов."""

from django.db.models import Count
from django.utils import timezone


def filter_published_posts(posts):
    """Оставить только опубликованные посты для публичного показа.

    Условия:
    - сам пост опубликован;
    - дата публикации не в будущем;
    - категория опубликована.
    Также добавляет аннотацию `comment_count` и оптимизирует выборки.
    """
    return posts.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
    ).annotate(
        comment_count=Count('comments')
    ).order_by(
        '-pub_date'
    ).select_related(
        'category', 'author', 'location'
    )
