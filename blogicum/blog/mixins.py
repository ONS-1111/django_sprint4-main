"""Переиспользуемые настройки и общая логика для CBV редактирования."""

from django.urls import reverse

from .models import Comment, Post


class PostsEditMixin:
    """Общие настройки для Create/Update/Delete постов."""

    model = Post
    template_name = 'blog/create.html'


class CommentEditMixin:
    """Общие настройки и переходы после операций с комментариями."""

    model = Comment
    pk_url_kwarg = 'comment_pk'
    template_name = 'blog/comment.html'

    def get_success_url(self):
        """После операции вернуть пользователя на страницу поста."""
        return reverse('blog:post_detail', args=[self.kwargs['post_id']])
