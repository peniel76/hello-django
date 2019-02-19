from django.urls import path
from shop.views import index, shop_detail     # from . import views 로도 가능

app_name = 'shop'  # URL Reverse에 사용

urlpatterns = [
    path('', index),
    path('<int:pk>/', shop_detail),
]