
from django.urls import path, register_converter
from blog.views import index, hello_times, articles_by_year

from blog.converters import FourDigitYearConverter, SlugUnicodeConverter

register_converter(FourDigitYearConverter, 'year')
#register_converter(SlugUnicodeConverter, 'unicode')

app_name = 'blog'  # URL Reverse에 사용

urlpatterns = [
    path('hello_times/<int:times>/', hello_times),
    path('', index),
    path('articles/<year:year>/', articles_by_year),
]