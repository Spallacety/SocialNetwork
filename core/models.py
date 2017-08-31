from django.db import models

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

class User(models.Model):
  name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  address = models.ForeignKey(Address, on_delete=models.CASCADE)

  class Meta:
    ordering = ('name',)

  def __str__(self):
    return self.name

class Post(models.Model):
  title = models.CharField(max_length=100)
  body = models.CharField(max_length=500)
  user = models.ForeignKey(User, related_name="posts")

  def __str__(self):
    return "%s posted %s" % (self.user.name, self.title)

class Comment(models.Model):
  name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  body = models.CharField(max_length=500)
  post = models.ForeignKey(Post, related_name="comments")

  def __str__(self):
    return "Comment from %s" % (self.name)