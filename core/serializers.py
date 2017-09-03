from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('url', 'email', 'username',)

class GeoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Geo
    fields = ('lat', 'lng',)

class AddressSerializer(serializers.HyperlinkedModelSerializer):
  geo = GeoSerializer()

  class Meta:
    model = Address
    fields = ('street', 'suite', 'city', 'zipcode', 'geo',)

class ProfileSerializer(serializers.ModelSerializer):
  address = AddressSerializer()
  user = UserSerializer()

  class Meta:
    model = Profile
    fields = ('url', 'name', 'user', 'address',)

class CommentSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Comment
    fields = ('url', 'name', 'email', 'body', 'post',)

class PostSerializer(serializers.HyperlinkedModelSerializer):
  profile = serializers.SlugRelatedField(read_only=True, slug_field='name')

  class Meta:
    model = Post
    fields = ('url', 'title', 'body', 'profile',)

class ProfileDetailSerializer(serializers.ModelSerializer):
  address = AddressSerializer()
  user = UserSerializer()
  posts = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='post-detail')

  class Meta:
    model = Profile
    fields = ('url', 'name', 'user', 'address', 'posts')

class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
  profile = serializers.SlugRelatedField(queryset=Profile.objects.all(), slug_field='name')
  comments = CommentSerializer(many=True, read_only=True)

  class Meta:
    model = Post
    fields = ('url', 'title', 'body', 'profile', 'comments',)