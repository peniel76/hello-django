from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

# accounts 앱은 app_name을 만들지 않음
#app_name = ""

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
]