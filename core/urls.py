from django.conf.urls import url

from .views import *

urlpatterns = [
  url(r'^$', APIRoot.as_view(), name='root'),
  url(r'^users/$', UserList.as_view(), name=UserList.name),
  url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view(),name=UserDetail.name),
  url(r'^address/$', AddressList.as_view(), name=AddressList.name),
  url(r'^address/(?P<pk>[0-9]+)/$', AddressDetail.as_view(), name=AddressDetail.name),
  url(r'^geo/$', GeoList.as_view(), name=GeoList.name),
  url(r'^geo/(?P<pk>[0-9]+)/$', GeoDetail.as_view(), name=GeoDetail.name),
  url(r'^posts/$', PostList.as_view(), name=PostList.name),
  url(r'^posts/(?P<pk>[0-9]+)/$', PostDetail.as_view(), name=PostDetail.name),
  url(r'^comments/$', CommentList.as_view(), name=CommentList.name),
  url(r'^comments/(?P<pk>[0-9]+)/$', CommentDetail.as_view(), name=CommentDetail.name),
]