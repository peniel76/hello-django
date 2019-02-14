from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import requests
from bs4 import BeautifulSoup

def index(request):
    return render(request, 'blog/index.html')

def hello_times(request, times):
    message = "안녕하세요" * times
    return HttpResponse(message)

def articles_by_year(request, year):
    return HttpResponse(f'''
        {year}년도에 대한 목록
    ''')

def naver_realtime_keywords(request):
    res = requests.get("http://naver.com")
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    tag_list = soup.select('.PM_CL_realtimeKeyword_rolling .ah_k')
    text = '<br/>\n'.join([tag.text for tag in tag_list])
    return HttpResponse(text)

def naver_blog_search(request):
    query = request.GET.get('query')

    url = 'https://search.naver.com/search.naver'

    params = {
        'where': 'post',
        'sm': 'tab_jum',
        'query': query,
    }

    res = requests.get(url, params=params)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')

    tag_list = soup.select('#elThumbnailResultArea .sh_blog_title')

    post_list = []
    for tag in tag_list:
        post_title = tag.text
        post_url = tag['href']
        post_list.append({
            'title': post_title,
            'url': post_url,
        })

    return render(request, 'blog/naver_blog_search.html', {
        'query': query,
        'post_list': post_list,
    })