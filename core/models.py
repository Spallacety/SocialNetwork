from django.db import models
from django.contrib.auth.models import User

class Geo(models.Model):
  lat = models.FloatField()
  lng = models.FloatField()

  def __str__(self):
    return "lat: %s, lng:%s" % (self.lat, self.lng)

class Address(models.Model):
  street = models.CharField(max_length=100)
  suite = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  zipcode = models.CharField(max_length=100)
  geo = models.ForeignKey(Geo, on_delete=models.CASCADE)

  class Meta:
    ordering = ('street', 'suite', 'city')

  def __str__(self):
    return "%s, %s, %s" % (self.street, self.suite, self.city)

class Profile(models.Model):
  name = models.CharField(max_length=100)
  address = models.ForeignKey(Address, on_delete=models.CASCADE)
  user = models.OneToOneField(User, related_name='user')

  @property
  def email(self):
    return self.user.email

  class Meta:
    ordering = ('name',)

  def __str__(self):
    return self.name

class Post(models.Model):
  title = models.CharField(max_length=100)
  body = models.CharField(max_length=500)
  profile = models.ForeignKey(Profile, related_name="posts", on_delete=models.CASCADE)

  def __str__(self):
    return "%s posted %s" % (self.profile.name, self.title)

class Comment(models.Model):
  name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  body = models.CharField(max_length=500)
  post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)

  def __str__(self):
    return "Comment from %s" % (self.email)