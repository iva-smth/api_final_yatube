from django.contrib.auth import get_user_model
from rest_framework import serializers, validators
from rest_framework.relations import SlugRelatedField
from posts.models import Comment, Post, Group, Follow


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')
        # Все поля только для чтения
        read_only_fields = ('id', 'title', 'slug', 'description')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        queryset=get_user_model().objects.all(),
        default=serializers.CurrentUserDefault()
    )
    #Отображается как username пользователя
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=get_user_model().objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')
        validators = (
            validators.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message=('Подписка уже существует')
            ),
        )

    def validate(self, data):
        # Проверка, что пользователь не пытается подписаться на самого себя.
        if data['user'] == data['following']:
            raise serializers.ValidationError(
                'Попытка подписаться на себя же'
            )
        return data

class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        read_only_fields = ('post',)
        model = Comment
