from django.db import models
#from django.contrib.auth.models import User

class Shop(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField(blank=True)
    address=models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    shop=models.ForeignKey(Shop, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    desc=models.TextField(blank=True)
    is_public=models.BooleanField(default=False)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
