from rest_framework import permissions
from users.backends import JWTAuthentication

class UserPostPermission(permissions.BasePermission):

    def has_permission(self,request,view):
        pass


    def has_object_permission(self,request,view,obj):
        pass
