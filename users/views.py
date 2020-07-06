from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import UserProfile, Post
from users.serializers import UserProfileSerializer, PostSerializer
from django.contrib import auth
import jwt
from django.conf import settings
from users.permissions import MustBeUser
from users.backends import JWTAuthentication
# Create your views here.

class CreatUserView(APIView):

    def post(self,request):
        serializer = UserProfileSerializer(data=request.data)

        if serializer.is_valid():
                user = UserProfile.objects.create_user(
                    email=request.data.get("email"),
                    password=request.data.get("password")
                )
                serializer_user = UserProfileSerializer(user)
                return Response(serializer_user.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class GetUsers(APIView):

    def get(self,request):
        users = UserProfile.objects.all()
        serializer = UserProfileSerializer(users, many=True)
        return Response(serializer.data)

class LoginUser(APIView):
    def post(self,request):
        user = auth.authenticate(email=request.data.get('email'),password=request.data.get('password'))

        if user:
            token = jwt.encode({'id':user.id,'email': user.email}, settings.SECRET_KEY)
            serializer = UserProfileSerializer(user)

            return Response({'data':serializer.data['email'], 'token': token}, status=status.HTTP_200_OK)

        return Response({'response': 'Invalid credentials'},status=status.HTTP_401_UNAUTHORIZED)


class UserPosts(APIView):
    authentication_classes = [JWTAuthentication]
    def get(self, request):
        user = request.user
        user_posts = user.posts.all()
        if len(user_posts) >= 1:
            serializer = PostSerializer(user_posts)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message':'No data found'}, status=status.HTTP_404_NOT_FOUND)
