from django.db import models
from posts.models import Post


class Comment(models.Model):
    text = models.TextField(
        'Текст'
    )
    post = models.ForeignKey(
        Post,
        verbose_name='Пост',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    date = models.DateField(
        'Дата',
        auto_now=True
    )

    def __str__(self):
        return self.text[:10]

    class Meta:
        ordering = ['-date']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        indexes = [
            models.Index(fields=['date', ])
        ]