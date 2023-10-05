from django.shortcuts import render
from .models import ProductList
from .forms import ProductListForm


def goods_index(request):
    data_goods = ProductList.objects.all()
    return render(request, 'goods/goods_index.html', {'data_goods': data_goods})


def add_product(request):
    link = 'goods/add_product.html'
    mess = ""
    if request.method == 'POST':
        form_goods = ProductListForm(request.POST)
        if form_goods.is_valid():
            form_goods.save()
            mess = "Запись добавлена"
            link = 'goods/goods_index.html'
        else:
            mess = "Неправильно заполнено"

    form_goods = ProductListForm()
    data = {
        'form_goods': form_goods,
        'mess': mess,
        'link': link
    }
    return render(request, data['link'], data)
