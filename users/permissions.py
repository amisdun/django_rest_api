from rest_framework import permissions
from users.backends import JWTAuthentication

class MustBeUser(permissions.BasePermission):
    authentication = JWTAuthentication.authenticate

    def has_permission(self,request,view):
        pass


    def has_object_permission(self,request,view,obj):
        self.authentication
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
