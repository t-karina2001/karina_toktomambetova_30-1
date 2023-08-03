from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from products.models import Product, Category, Review
from products.forms import ProductCreateForm, CategoryCreateForm, ReviewCreateForm

from products.constants import PAGINATION_LIMIT


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        max_page = products.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        search_text = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if search_text:
            products = products.filter(Q(title__icontains=search_text) |
                                       Q(description__icontains=search_text))

        products = products[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

        context_data = {
            'products': products,
            'user': request.user,
            'pages': range(1, max_page+1)
        }
        return render(request, 'products/products.html', context=context_data)


def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()

        context_data = {
            'categories': categories
        }

        return render(request, 'categories/categories.html', context=context_data)


def product_detail_view(request, id):
    if request.method == "GET":
        product = Product.objects.get(id=id)

        context_data = {
            'product': product
        }

        return render(request, 'products/detail.html', context=context_data)


@login_required
def product_create_view(request):
    if request.method == 'GET':
        context_data = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=context_data)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = ProductCreateForm(data, files)

        if form.is_valid():
            Product.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price'),
                rate=form.cleaned_data.get('rate'),
            )
            return redirect('/products/')

        return render(request, 'products/create.html', context={
            'form': form
        })


def category_create_view(request):
    if request.method == 'GET':
        context_data = {
            'form': CategoryCreateForm
        }
        return render(request, 'products/categories.html', context=context_data)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = CategoryCreateForm(data, files)

        if form.is_valid():
            Category.objects.create(
                title=form.cleaned_data.get('title'),
            )
            return redirect('/categories/')

        return render(request, 'products/categories.html', context={
            'form': form
        })


def review_create_view(request, id):
    if request.method == 'GET':
        context_data = {
            'form': ReviewCreateForm
        }
        return render(request, 'products/reviews.html', context=context_data)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = ReviewCreateForm(data, files)

        if form.is_valid():
            product = Product.objects.get(id=id)
            Review.objects.create(
                user_name=form.cleaned_data.get('user_name'),
                e_mail=form.cleaned_data.get('e_mail'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate'),
                product=product,

            )
            return redirect('products/detail.html'.format(id))

        return render(request, 'products/reviews.html', context={
            'form': form
        })
