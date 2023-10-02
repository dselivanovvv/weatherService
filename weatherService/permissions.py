from rest_framework.permissions import BasePermission

from weatherService.settings import X_TOKEN


class ConstTokenDjangoPermission(BasePermission):

    def has_permission(self, request, view):
        if request.headers.get('X-Token', None) == X_TOKEN:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
