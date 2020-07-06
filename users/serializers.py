from rest_framework import serializers
from users.models import UserProfile,Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','titile','author']


class UserProfileSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)
    class Meta:
        model = UserProfile
        fields = ['id','email','password','posts']
