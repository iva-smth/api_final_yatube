from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

"""
Модель подписок. Связывает пользователей: кто на кого подписан.

Поля:
    user (ForeignKey): Пользователь, который подписывается.
    following (ForeignKey): Пользователь, на которого подписываются.
"""
class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
    )

"""
Модель групп для объединения постов по тематике.

Поля:
    title (CharField): Название группы.
    slug (SlugField): Уникальный идентификатор для URL.
    description (TextField): Описание группы.
"""
class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title

"""
Модель публикаций (постов).

Поля:
    text (TextField): Текст поста.
    pub_date (DateTimeField): Дата публикации.
    author (ForeignKey): Автор поста.
    image (ImageField): Изображение (необязательное).
    group (ForeignKey): Группа, к которой относится пост (необязательно).
"""
class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
    )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True
    )
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name='posts',
        null=True, blank=True
    )

    def __str__(self):
        return self.text

"""
Модель комментариев к постам.

Поля:
    author (ForeignKey): Автор комментария.
    post (ForeignKey): Пост, к которому относится комментарий.
    text (TextField): Текст комментария.
    created (DateTimeField): Дата создания комментария.
"""
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
