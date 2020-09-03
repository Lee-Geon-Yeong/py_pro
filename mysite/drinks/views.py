from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from django.http.response import JsonResponse
from django.shortcuts import get_list_or_404
from django.http import HttpResponseBadRequest, response,HttpRequest,HttpResponseRedirect
from drinks.models import Drinks, Brand
from django.views.decorators.http import require_GET, require_http_methods
from django.contrib.auth.decorators import login_required
from drinks.filters import DrinkFilter
from django.db.models import Q, Prefetch
from django.urls import reverse_lazy
from carts.views import create_cart_item, get_cart_and_items
from .forms import CartItemCreateForm

@require_GET
def index_view(request):
    objects = Drinks.objects.all().order_by('-likes')[:24]
    return render(request,template_name='drinks/index.html',context={"objects":objects})

@require_GET
def list_filter_view(request):
    PAGE_SIZE = 1
    objects = Drinks.objects.select_related('brand') 
    f = DrinkFilter(request.GET, queryset=objects) # 1.49ms
    paginator = Paginator(f.qs, PAGE_SIZE)
    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)
    return render(request,template_name='drinks/list.html',context={'filter':f, 'objects':response})

@require_GET
def brand_detail_view(request, brand_name):
    objects = Brand.objects.prefetch_related(Prefetch('drinks')).get(name=brand_name)
    return render(request,template_name='drinks/brand.html', context={'object':objects})


@login_required
@require_http_methods(['GET', 'POST'])
def drink_detail_view(request, pk):
    if request.method == 'POST':
        amount = request.POST.get('quantity')
        form = CartItemCreateForm(request.POST)
        if form.is_valid():
            user_cart = get_cart_and_items(request)
            created = create_cart_item(pk, form.cleaned_data['quantity'], user_cart)
        return HttpResponseRedirect(reverse_lazy('mypage:index'))
    form = CartItemCreateForm()
    return render(request, template_name="drinks/detail.html", context={'object':Drinks.objects.prefetch_related(Prefetch('posts')).get(id=pk), 'form':form})
