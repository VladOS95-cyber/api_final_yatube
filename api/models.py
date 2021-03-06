from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(
        "Дата публикации", auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField()
    created = models.DateTimeField(
        "Дата добавления", auto_now_add=True, db_index=True
    )


class Group(models.Model):
    title = models.CharField(
        verbose_name='Название группы',
        max_length=200,
        help_text='Напишите название группы'
    )
    slug = models.SlugField(
        verbose_name='Слаг',
        max_length=50,
        unique=True,
        help_text='Укажите адрес для страницы задачи.'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Добавьте описание группы'
    )

    def __str__(self):
        return self.title


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Имя подписчика',
        related_name='follower',
        help_text='Имя подписчика добавляется автоматически'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Имя подписанта',
        related_name='following',
        help_text='Имя подписанта добавляется автоматически'
    )

    class Meta:
        unique_together = ['user', 'following']
