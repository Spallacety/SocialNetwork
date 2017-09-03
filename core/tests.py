from django.test import *
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework.test import *
from rest_framework import status

class APITest(TestCase):

  fixtures = ['fixtures.json']

  def test_profile_list(self):
    response = self.client.get(reverse('profile-list'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_profile_detail(self):
    response = self.client.get(reverse('profile-detail', args=[1]))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_post_list(self):
    response = self.client.get(reverse('post-list'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_post_detail(self):
    response = self.client.get(reverse('post-detail', args=[1]))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_comment_list(self):
    response = self.client.get(reverse('comment-list'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_comment_detail(self):
    response = self.client.get(reverse('comment-detail', args=[1]))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_new_profile(self):
    request_data = {"id": 1,
                    "username": "Bret",
                    "email": "Sincere@april.biz",
                    "name": "Leanne Graham"}
    response = self.client.put(reverse('profile-list'), data=request_data)
    self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

  def test_new_post_auth(self):
    self.client.post('/api-auth/login/', {'username': 'Bret', 'password': 'xpto'})
    request_data = {"title": "new post",
                    "body": "body of post"}
    response = self.client.post(reverse('post-list'), request_data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

  def test_new_post_not_auth(self):
    request_data = {"title": "new post",
                    "body": "body of post"}
    response = self.client.post(reverse('post-list'), request_data, format='json')
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_new_comment(self):
    request_data = {"name": "new comment",
                    "email": "new@comment.com",
                    "body": "body of comment",
                    "post": "http://localhost/post/2/"}
    response = self.client.post(reverse('comment-list'), request_data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

  def test_delete_comment_owner(self):
    self.client.post('/api-auth/login/', {'username': 'Bret', 'password': 'xpto'})
    response = self.client.delete(reverse('comment-detail', args=[2]))
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

  def test_delete_comment_not_owner(self):
    self.client.post('/api-auth/login/', {'username': 'Bret', 'password': 'xpto'})
    response = self.client.delete(reverse('comment-detail', args=[101]))
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)