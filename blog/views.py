from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import requests
import os
from bs4 import BeautifulSoup

from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

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
    query = request.GET.get('query', '')
    post_list=[]

    if query:
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

def 이미지생성응답(request):
    #ttf_path = 'C:/Windows/Fonts/malgun.ttf' # 윈도우, 맥:
    ttf_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets/Fonts/AppleGothic.ttf') #'assets/Fonts/AppleGothic.ttf'

    image_url = 'http://www.flowermeaning.com/flower-pics/Calla-Lily-Meaning.jpg'
    #image_url = 'assets/images/s1.jpg'

    res = requests.get(image_url) # 서버로 HTTP GET 요청하여, 응답 획득

    io = BytesIO(res.content) # 응답의 Raw Body  메모리 파일 객체 BytesIO 인스턴스 생성
    io.seek(0) # 파일의 처음으로 커서를 이동
    canvas = Image.open(io).convert('RGBA') # 이미지 파일을 열고, RGBA 모드로 변환
    font = ImageFont.truetype(ttf_path, 15) # 지정 경로의 TrueType 폰트, 폰트크기 40
    draw = ImageDraw.Draw(canvas) # canvas에 대한 ImageDraw 객체 획득

    text = request.GET.get('name', '익명')
    left, top = 10, 10
    margin = 10
    width, height = font.getsize(text)
    right = left + width + margin
    bottom = top + height + margin

    draw.rectangle((left, top, right, bottom), (255, 255, 224))
    draw.text((15,15), text, font=font, fill=(20, 20, 20))

    response = HttpResponse(content_type='image/png')
    canvas.save(response, format='PNG')

    return response
