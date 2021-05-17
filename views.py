from django.shortcuts import render
from .models import ProductCategory, Product

def products(request):
    links_menu = {'links': [
        {'href': 'index', 'name': 'все'},
        {'href': 'index', 'name': 'дом'},
        {'href': 'index', 'name': 'офис'},
        {'href': 'index', 'name': 'модерн'},
        {'href': 'index', 'name': 'классика'}
    ]}
    return render(request, 'products.html',context=links_menu )
# context=links_menu

def main(request):
    title = 'главная'

    products = Product.objects.all()[:4]

    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)