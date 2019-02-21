from django.urls import reverse
from django.db import models
#from django.contrib.auth.models import User

class Shop(models.Model):
    name=models.CharField(max_length=100)
    photo = models.ImageField(blank=True)
    desc=models.TextField(blank=True)
    address=models.CharField(max_length=50, blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return "/shop/{}/".format(self.id)
        return reverse("shop:shop_detail", args=[self.id])
        # return reverse("shop:shop_detail", kwargs={'pk': self.id})


class Item(models.Model):
    shop=models.ForeignKey(Shop, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    desc=models.TextField(blank=True)
    price=models.PositiveIntegerField()
    is_public=models.BooleanField(default=False)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
