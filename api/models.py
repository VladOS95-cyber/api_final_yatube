from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        verbose_name='Название группы',
        max_length=200,
        help_text='Напишите название группы'
    )

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
    )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        verbose_name='Группа',
        help_text='Выберите группу',
        blank=True, null=True,
        related_name='posts'
    )

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Имя подписчика',
        related_name='user',
        help_text='Имя подписчика добавляется автоматически'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Имя подписанта',
        related_name='following',
        help_text='Имя подписанта добавляется автоматически'
    )
