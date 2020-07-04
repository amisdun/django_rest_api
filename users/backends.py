import jwt
from rest_framework import authentication,exceptions
from rest_framework.response import Response
from django.conf import settings
from users.models import UserProfile

class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self,request):
        auth_data = authentication.get_authorization_header(request)

        if not auth_data:
            return None
        prefix,token = auth_data.decode('utf-8').split(' ')

        try:
            payload = jwt.decode(token, settings.SECRET_KEY)

            user = UserProfile.objects.get(id=payload['id'])

            return (user,token)
        except jwt.DecodeError as e:
            raise exceptions.AuthenticationFailed('your token is invalid')
        except jwt.ExpiredSignatureError as e:
            raise exceptions.AuthenticationFailed('your token is invalid')
        return super().authenticate(request)
