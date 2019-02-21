from django.urls import path
#from shop.views import index, shop_detail     # from . import views 로도 가능
from . import views

app_name = 'shop'  # URL Reverse에 사용

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.shop_detail),
    path('new/', views.shop_new),
    path('new2/', views.shop_new_cbv),
    path('<int:pk>/edit/', views.shop_edit),
    path('<int:pk>/edit2/', views.shop_edit_cbv),
    #path('<int:pk>/delete', views.shop_delete),
]