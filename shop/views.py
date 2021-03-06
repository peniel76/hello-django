from django.shortcuts import render, redirect, get_object_or_404
from .models import Shop
from .forms import ShopForm, ItemForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.

# def index(request):
#     #전체 Shop목록을 가져올 예정
#     qs=Shop.objects.all().order_by('id')
#     return render(request, 'shop/shop_list.html', {
#         'shop_list':qs
#     })

#index = ListView.as_view(model=Shop)

class PostListView(ListView):   # 확정시 용이함
    model = Shop

    def get_context_data(self):
        context = super().get_context_data()
        context.update({
            'hello': 'world',
        })
        return context

index = PostListView.as_view()

# def shop_detail(request, pk):
#     shop=Shop.objects.get(pk=pk)
#     return render(request, 'shop/shop_detail.html', {
#         'shop':shop,
#     })

shop_detail = DetailView.as_view(model=Shop)

@login_required  #-> 장식자를 통해서 로그인 시에만 shop_new만 실행되도록 함
def shop_new(request):
    form_cls = ShopForm
    #form_cls2 = ItemForm

    if request.method == "POST":   # GET 빈폼 or POST 반드시 입력 받음
        form = form_cls(request.POST, request.FILES, prefix="shop")
        #form2 = form_cls2(request.POST, request.FILES, prefix="item")
        if form.is_valid(): #and form2.is_valid(): # 밸리드 체크 시 오류가 없을 경우에만 True리턴
            shop = form.save(commit=False) # 폼에 입력된 값을 저장, commit=FALSE를 사용하면 아래에 지정한 필드에 대해서는 save 제외됨
            shop.user = request.user   # user 필드를 자동으로 세팅함
            shop.save()
            #form2.save()
            #return redirect('/shop/{}/'.format(shop.id))
            return redirect(shop)  # get_absolute_url 적용됨
    else:
        form = form_cls(prefix="shop")
        #form2 = form_cls2(prefix="item")

    return render(request, 'shop/shop_form.html', {
        'form':form,
        #'form2':form2,
    })

#shop_new와 동일한 역할 수행함
# shop_new_cbv = CreateView.as_view(
#     model=Shop, form_class=ShopForm,
#     success_url= '/shop/')
# models.py에서 해당 모델에 대한 get_absolute_URL이 정의되어 있으면 success_url이 없어도됨
shop_new_cbv = CreateView.as_view(
    model=Shop, form_class=ShopForm) # get_absolute_url 적용됨

@login_required
def shop_edit(request, pk):
    # try:
    #     shop = Shop.objects.get(pk=pk)  #입력된 PK의 값을 가져옮
    # except Shop.DoesNotExist:
    #     raise Http404
    shop = get_object_or_404(Shop, pk=pk)  #에러처리 포함된 코드

    if request.user != shop.user: # 최종 작성자와 수정자가 다를 경우
        return redirect(shop)

    form_cls = ShopForm

    if request.method == "POST":   # GET 빈폼 or POST 반드시 입력 받음
        form = form_cls(request.POST, request.FILES, instance=shop)
        if form.is_valid(): # 밸리드 체크 시 오류가 없을 경우에만 True리턴
            shop = form.save() # 폼에 입력된 값을 저장
            #return redirect('/shop/{}/'.format(shop.id))
            return redirect(shop) # get_absolute_url 적용됨
    else:
        form = form_cls(instance=shop)

    return render(request, 'shop/shop_form.html', {
        'form':form,
    })

# shop_edit_cbv = UpdateView.as_view(
#     model=Shop, form_class=ShopForm,
#     success_url='/shop/'
# )
# models.py에서 해당 모델에 대한 get_absolute_URL이 정의되어 있으면 success_url이 없어도됨
shop_edit_cbv = UpdateView.as_view(
    model=Shop, form_class=ShopForm) # get_absolute_url 적용됨

@login_required
def shop_delete(request, pk): #(user=request.user)로 하면 미 일치시 404 에러 발생
    shop = get_object_or_404(Shop, pk=pk)

    if request.user != shop.user: # 최종 작성자와 수정자가 다를 경우
        return redirect(shop)

    if request.method == 'POST':
        shop.delete()
        return redirect('shop:index')

    return render(request, 'shop/shop_confirm_delete.html', {
        'shop': shop,
    })

shop_delete_cbv = DeleteView.as_view(model=Shop,
    success_url=reverse_lazy('shop:index'))