from django.db import models

class Category(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.CharField(unique = True, blank = True, null = True)

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.CharField(unique = True, blank = True, null = True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateField(auto_now = True)
