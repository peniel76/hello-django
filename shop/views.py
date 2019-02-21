from django.shortcuts import render, redirect, get_object_or_404
from .models import Shop
from .forms import ShopForm, ItemForm
from django.views.generic import CreateView, UpdateView
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

def shop_new(request):
    form_cls = ShopForm
    #form_cls2 = ItemForm

    if request.method == "POST":   # GET 빈폼 or POST 반드시 입력 받음
        form = form_cls(request.POST, request.FILES)
        #form2 = form_cls2(request.POST, request.FILES)
        if form.is_valid() and form2.is_valid(): # 밸리드 체크 시 오류가 없을 경우에만 True리턴
            shop = form.save() # 폼에 입력된 값을 저장
            #form2.save()
            return redirect('/shop/{}/'.format(shop.id))
    else:
        form = form_cls()
        #form2 = form_cls2()

    return render(request, 'shop/shop_form.html', {
        'form':form,
        #'form2':form2,
    })

#shop_new와 동일한 역할 수행함
shop_new_cbv = CreateView.as_view(
    model=Shop, form_class=ShopForm,
    success_url= '/shop/')

def shop_edit(request, pk):
    # try:
    #     shop = Shop.objects.get(pk=pk)  #입력된 PK의 값을 가져옮
    # except Shop.DoesNotExist:
    #     raise Http404
    shop = get_object_or_404(Shop, pk=pk)  #에러처리 포함된 코드

    form_cls = ShopForm

    if request.method == "POST":   # GET 빈폼 or POST 반드시 입력 받음
        form = form_cls(request.POST, request.FILES, instance=shop)
        if form.is_valid(): # 밸리드 체크 시 오류가 없을 경우에만 True리턴
            shop = form.save() # 폼에 입력된 값을 저장
            return redirect('/shop/{}/'.format(shop.id))
    else:
        form = form_cls(instance=shop)

    return render(request, 'shop/shop_form.html', {
        'form':form,
    })

shop_edit_cbv = UpdateView.as_view(
    model=Shop, form_class=ShopForm,
    success_url='/shop/'
)