"""Формы создания/редактирования постов и комментариев."""

from django import forms
from django.utils import timezone

from .models import Comment, Post


class CreatePostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:
            self.fields['is_published'].initial = True

    """Форма создания/редактирования поста.

    Поле `pub_date` с HTML5‑виджетом datetime-local для поддержки
    публикаций «задним числом» и отложенных публикаций.
    """

    pub_date = forms.DateTimeField(
        initial=timezone.now,
        required=True,
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
            },
            format='%Y-%m-%dT%H:%M',
        ),
    )

    class Meta:
        model = Post
        fields = (
            'title',
            'image',
            'text',
            'pub_date',
            'location',
            'category',
            'is_published',
        )


class CreateCommentForm(forms.ModelForm):
    """Минимальная форма создания/редактирования комментария."""

    class Meta:
        model = Comment
        fields = ("text",)
