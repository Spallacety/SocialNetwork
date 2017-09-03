from rest_framework import permissions
from .models import *

class OwnerPostPermissionsOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    else:
      return obj.profile.user == request.user

class OwnerPostCommentPermissionsOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    else:
      if obj.post.profile.user == request.user:
        if request.method == 'DELETE':
          return True
        else:
          return False
      return False