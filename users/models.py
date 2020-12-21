from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    slug = models.SlugField(unique=True)
    image = models.FileField(upload_to="post_image", blank=True)
    summary = models.TextField()



