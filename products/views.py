from django.shortcuts import render

from products.models import Product, Category


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        product = Product.objects.all()

        context_data = {
            'products': product
        }
        return render(request, 'products/products.html', context=context_data)


def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()

        context_data = {
            'categories': categories
        }

        return render(request, 'categories/categories.html', context=context_data)