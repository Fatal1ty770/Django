from django.shortcuts import render
from mainapp.models import ProductCategory, Product


def main(request):
    products = Product.objects.all()[:4]

    context = {
        'slogan': 'Супер УДОБНЫЕ СТУЛЬЯ',
        'topic': 'Тренды',
        'products': products,
    }
    return render(request, 'index.html', context=context)



    #
    # content = {'title': title, 'products': products}
    # return render(request, 'mainapp/index.html', content)


def contacts(request):
    return render(request, 'contacts.html')