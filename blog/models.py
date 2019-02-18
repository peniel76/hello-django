from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings  # 설정값을 가져오는 올바른 방법

# settings --> auth
# django/django/conf/global_settings.py  --> auth.User 활용

# Create your models here.
class Post(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title=models.CharField(max_length=100, db_index=True)
    contents=models.TextField()
    tags=models.CharField(max_length=20)
    is_publish=models.BooleanField(default=False)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ost=models.ForeignKey(Post, on_delete=models.CASCADE)
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