from django.urls import reverse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import *
from .models import *
from .permissions import *

# import json
# from django.urls import reverse
# from django.utils import timezone
# from rest_framework import status, generics, viewsets
# from rest_framework.decorators import api_view
# from rest_framework.generics import get_object_or_404
# from rest_framework.response import Response
# from django.shortcuts import render
# from rest_framework.views import APIView

class UserList(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  name = 'user-list'

class UserDetail(generics.RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  name = 'user-detail'

class ProfileList(generics.ListAPIView):
  queryset = Profile.objects.all()
  serializer_class = ProfileSerializer
  name = 'profile-list'

class ProfileDetail(generics.RetrieveAPIView):
  queryset = Profile.objects.all()
  serializer_class = ProfileDetailSerializer
  name = 'profile-detail'

class PostList(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  name = 'post-list'
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

  def perform_create(self, serializer):
    profile = Profile.objects.get(user=self.request.user)
    serializer.save(profile=profile)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Post.objects.all()
  serializer_class = PostDetailSerializer
  name = 'post-detail'
  permission_classes = (OwnerPostPermissionsOrReadOnly,)

class CommentList(generics.ListCreateAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  name = 'comment-list'

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  name = 'comment-detail'
  permission_classes = (OwnerPostCommentPermissionsOrReadOnly,)

class AddressList(generics.ListAPIView):
  queryset = Address.objects.all()
  serializer_class = AddressSerializer
  name = 'address-list'

class AddressDetail(generics.RetrieveAPIView):
  queryset = Address.objects.all()
  serializer_class = AddressSerializer
  name = 'address-detail'

class GeoList(generics.ListAPIView):
  queryset = Geo.objects.all()
  serializer_class = GeoSerializer
  name = 'geo-list'

class GeoDetail(generics.RetrieveAPIView):
  queryset = Geo.objects.all()
  serializer_class = GeoSerializer
  name = 'geo-detail'

class APIRoot(generics.GenericAPIView):
  def get(self, request):
    return Response({'profiles': reverse(ProfileList.name, request=request),
                     'posts': reverse(PostList.name, request=request),
                     'comments': reverse(CommentList.name, request=request),
                     'users': reverse(UserList.name, request=request)
                     })

def import_data():
  dump_data = open('db.json', 'r')
  as_json = json.load(dump_data)

  # Post as json
  # {
  #   "user_id": 1,
  #   "id": 1,
  #   "title": "",
  #   "body": "",
  # },

  # Comment as json
  # {
  #     "post_id": 1,
  #     "id": 1,
  #     "name": "",
  #     "email": "",
  #     "body": "",
  # },

  # User as json
  # {
  #     "id": 1,
  #     "name": "Leanne Graham",
  #     "username": "Bret",
  #     "email": "Sincere@april.biz",
  #     "address": {
  #         "street": "Kulas Light",
  #         "suite": "Apt. 556",
  #         "city": "Gwenborough",
  #         "zipcode": "92998-3874",
  #         "geo": {
  #             "lat": "-37.3159",
  #             "lng": "81.1496"
  #         }
  #     }
  # }

  for profile in as_json['users']:
    geo = Geo.objects.create(lat=profile['address']['geo']['lat'],
                             lng=profile['address']['geo']['lng'])
    address = Address.objects.create(street=profile['address']['street'],
                                     suite=profile['address']['suite'],
                                     city=profile['address']['city'],
                                     zipcode=profile['address']['zipcode'],
                                     geo=geo)
    user = User.objects.create_user(profile['username'],
                                    email=profile['email'],
                                    password='xpto')
    Profile.objects.create(id=profile['id'],
                        name=profile['name'],
                        address=address,
                        user=user)

  for post in as_json['posts']:
    profile = Profile.objects.get(id=post['userId'])
    Post.objects.create(id=post['id'],
                        title=post['title'],
                        body=post['body'],
                        profile=profile)

  for comment in as_json['comments']:
    post = Post.objects.get(id=comment['postId'])
    Comment.objects.create(id=comment['id'],
                           name=comment['name'],
                           email=comment['email'],
                           body=comment['body'],
                           post=post)