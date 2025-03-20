from rest_framework import permissions


class OwnershipPermission(permissions.BasePermission):
    """
    Пользовательское разрешение для проверки прав доступа.

    - Разрешает доступ к безопасным методам (GET, HEAD, OPTIONS) всем пользователям.
    - Для небезопасных методов (POST, PUT, DELETE и т.д.) требуется аутентификация.
    - На уровне объекта разрешает доступ только автору объекта.
    """

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
