from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, pagination, permissions, viewsets
from posts.models import Post, Group, Comment, Follow
from .serializers import (
    PostSerializer,
    GroupSerializer,
    CommentSerializer,
    FollowSerializer
)
from .permissions import OwnershipPermission

class FollowViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin
):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)  # Требуется аутентификация
    filter_backends = (filters.SearchFilter,)  # Поддержка поиска
    search_fields = ('following__username',)  # Поиск по имени пользователя

    def get_queryset(self):
        # Возвращает только подписки текущего пользователя.
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PermissionViewset(viewsets.ModelViewSet):
    permission_classes = (OwnershipPermission,)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(PermissionViewset):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return self.get_post_obj().comments.all()

    def get_post_obj(self):
        # Получает объект поста по его ID или возвращает ошибку 404, если пост не найден.
        return get_object_or_404(
            Post,
            pk=self.kwargs.get('post_pk')
        )

    def perform_create(self, serializer):
        # При создании комментария автор и пост автоматически устанавливаются.
        return serializer.save(
            author=self.request.user,
            post=self.get_post_obj()
        )

class PostViewSet(PermissionViewset):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = pagination.LimitOffsetPagination  

    def perform_create(self, serializer):
        # При создании поста автор автоматически устанавливается как текущий пользователь.
        return serializer.save(author=self.request.user)
