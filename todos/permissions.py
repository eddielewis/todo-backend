from rest_framework import permissions
from .models import Todo


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


"""
class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # return obj.user == request.user
        return False
"""
