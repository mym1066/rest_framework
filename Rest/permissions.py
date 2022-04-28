from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    message = 'permission denied, you are not the owner'

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:#شامل  GET, HEAD or OPTIONS
            return True
        return obj.user == request.user



#from rest_framework import permissions


#class IsOwnerOrReadOnly(permissions.BasePermission):
#    message = 'permission denied, you are not the owner'
#
#   def has_permission(self, request, view):
#        return request.user.is_authenticated and request.user

#    def has_object_permission(self, request, view, obj):
#        if request.method in permissions.SAFE_METHODS:#شامل  GET, HEAD or OPTIONS
#            return True
#        return obj.user == request.user
