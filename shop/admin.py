from django.contrib import admin
from .models import Shop, Item
# Register your models here.

#admin.site.register(Shop)
@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'desc']
    list_display_links=['name']
    search_fields=['name']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display=['id','name', 'item_content']
    list_display_links=['name']

    def item_content(self, shop):
        return shop.desc[:20] + '...'
#admin.site.register(Item)