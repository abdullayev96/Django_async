from rest_framework import permissions


class IsAdminUser(permissions.BasePermission):
    """
    Faqat adminlar uchun (is_staff).
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Agar viewda 'action' atributi bo'lsa (ViewSet bo'lsa), tekshiramiz
        action = getattr(view, 'action', None)

        if action in ['list', 'destroy']:
            return bool(request.user and request.user.is_staff)

        # Agar bu APIView bo'lsa (action yo'q),
        # faqat login bo'lganini tekshiramiz
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        is_owner = (obj == request.user) if hasattr(obj, 'pk') else (getattr(obj, 'user', None) == request.user)
        is_admin = bool(request.user and request.user.is_staff)
        return is_owner or is_admin