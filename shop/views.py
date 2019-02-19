from django.shortcuts import render
from .models import Shop
# Create your views here.

def index(request):
    #전체 Shop목록을 가져올 예정
    qs=Shop.objects.all().order_by('id')
    return render(request, 'shop/shop_list.html', {
        'shop_list':qs
    })

def shop_detail(request, pk):
    shop=Shop.objects.get(pk=pk)
    return render(request, 'shop/shop_detail.html', {
        'shop':shop,
    })