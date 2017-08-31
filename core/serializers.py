from rest_framework import serializers
from .models import *

class GeoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Geo
    fields = ('url', 'lat', 'lng',)

class AddressSerializer(serializers.HyperlinkedModelSerializer):
  geo = GeoSerializer()

  class Meta:
    model = Address
    fields = ('url', 'street', 'suite', 'city', 'zipcode', 'geo',)

class UserSerializer(serializers.ModelSerializer):
  address = AddressSerializer()

  class Meta:
    model = User
    fields = ('url', 'name', 'email', 'address',)

class CommentSerializer(serializers.HyperlinkedModelSerializer):
  post = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='title')

  class Meta:
    model = Comment
    fields = ('url', 'name', 'email', 'body', 'post',)

class PostSerializer(serializers.HyperlinkedModelSerializer):
  user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

  class Meta:
    model = Post
    fields = ('url', 'title', 'body', 'user',)

class UserDetailSerializer(serializers.ModelSerializer):
  address = AddressSerializer()
  posts = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='post-detail')

  class Meta:
    model = User
    fields = ('url', 'email', 'name', 'address', 'posts')

class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
  user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
  comments = CommentSerializer(many=True, read_only=True)

  class Meta:
    model = Post
    fields = ('url', 'title', 'body', 'user', 'comments',)