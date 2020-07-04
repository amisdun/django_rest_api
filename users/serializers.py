from rest_framework import serializers
from users.models import UserProfile,Post

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','email','password']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','user','titile','author']
