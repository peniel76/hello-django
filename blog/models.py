from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    contents=models.TextField()
    tags=models.CharField(max_length=20)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    author_name=models.CharField(max_length=100)
    message=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

"""
class ZipCode(models.Model):
    #code=models.CharField(max_length=6, primary_key=True)
    code=models.CharField(max_length=6, unique=True)
    desc=models.TextField()
"""