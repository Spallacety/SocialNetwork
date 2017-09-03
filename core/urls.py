from django.conf.urls import url

from .views import *

urlpatterns = [
  url(r'^$', APIRoot.as_view(), name='root'),
  url(r'^profiles/$', ProfileList.as_view(), name=ProfileList.name),
  url(r'^profile/(?P<pk>[0-9]+)/$', ProfileDetail.as_view(),name=ProfileDetail.name),
  url(r'^users/$', UserList.as_view(), name=UserList.name),
  url(r'^user/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name=UserDetail.name),
  url(r'^addresses/$', AddressList.as_view(), name=AddressList.name),
  url(r'^address/(?P<pk>[0-9]+)/$', AddressDetail.as_view(), name=AddressDetail.name),
  url(r'^geos/$', GeoList.as_view(), name=GeoList.name),
  url(r'^geo/(?P<pk>[0-9]+)/$', GeoDetail.as_view(), name=GeoDetail.name),
  url(r'^posts/$', PostList.as_view(), name=PostList.name),
  url(r'^post/(?P<pk>[0-9]+)/$', PostDetail.as_view(), name=PostDetail.name),
  url(r'^comments/$', CommentList.as_view(), name=CommentList.name),
  url(r'^comment/(?P<pk>[0-9]+)/$', CommentDetail.as_view(), name=CommentDetail.name),
]