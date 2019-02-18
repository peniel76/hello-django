from django.contrib import admin
from .models import Shop, Item
# Register your models here.

#admin.site.register(Shop)
@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'desc']
    list_display_links=['name']
    search_fields=['name']

admin.site.register(Item)