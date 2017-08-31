from django.urls import reverse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import *
from .models import *

class UserList(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  name = 'user-list'

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserDetailSerializer
  name = 'user-detail'

class PostList(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  name = 'post-list'

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Post.objects.all()
  serializer_class = PostDetailSerializer
  name = 'post-detail'

class CommentList(generics.ListCreateAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  name = 'comment-list'

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  name = 'comment-detail'

class AddressList(generics.ListCreateAPIView):
  queryset = Address.objects.all()
  serializer_class = AddressSerializer
  name = 'address-list'

class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Address.objects.all()
  serializer_class = AddressSerializer
  name = 'address-detail'

class GeoList(generics.ListCreateAPIView):
  queryset = Geo.objects.all()
  serializer_class = GeoSerializer
  name = 'geo-list'

class GeoDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Geo.objects.all()
  serializer_class = GeoSerializer
  name = 'geo-detail'

class APIRoot(generics.GenericAPIView):
  def get(self, request):
    return Response({'users': reverse(UserList.name, request=request),
                     'address': reverse(AddressList.name, request=request),
                     'geo': reverse(GeoList.name, request=request),
                     'posts': reverse(PostList.name, request=request),
                     'comments': reverse(CommentList.name, request=request)
                     })