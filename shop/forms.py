from django import forms
from .models import Shop, Item

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'   # 모든 필드 가져와서 폼으로 처리  fields = ['title','contents']


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'