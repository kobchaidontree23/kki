from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    pos = models.CharField(max_length=200)

class Review(models.Model):
    reviews = models.CharField(max_length=200)


# class Register(models.Model):
#     username = models.CharField(max_length=100)
#     firstname = models.CharField(max_length=200)
#     lastname = models.CharField(max_length=200)
#     password = models.TextField()
#     repassword = models.TextField()
#     email = models.TextField()