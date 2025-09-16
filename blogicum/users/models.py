"""Кастомная модель пользователя (наследуемся от AbstractUser).

Дополнительно определён `get_absolute_url` для перехода в профиль.
"""

from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    def get_absolute_url(self):
        """Ссылка на публичную страницу профиля пользователя."""
        return reverse('blog:profile', kwargs={'username': self.username})
