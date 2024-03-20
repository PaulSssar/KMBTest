# Generated by Django 5.0.3 on 2024-03-20 08:16

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("header", models.CharField(max_length=65, verbose_name="Заголовок")),
                ("text", models.TextField(verbose_name="Текст")),
                (
                    "date",
                    models.DateField(auto_now=True, verbose_name="Дата публикации"),
                ),
            ],
            options={
                "verbose_name": "Пост",
                "verbose_name_plural": "Посты",
                "ordering": ["-date", "header"],
                "indexes": [
                    models.Index(fields=["date"], name="posts_post_date_fb749e_idx")
                ],
            },
        ),
    ]