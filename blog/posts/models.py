from django.db import models


class Post(models.Model):
    header = models.CharField(
        'Заголовок',
        max_length=65
    )
    text = models.TextField(
        'Текст',
    )
    date = models.DateField(
        'Дата публикации',
        auto_now=True
    )

    def __str__(self):
        return self.header

    class Meta:
        ordering = ['-date', 'header']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        indexes = [
            models.Index(fields=['date', ])
        ]
