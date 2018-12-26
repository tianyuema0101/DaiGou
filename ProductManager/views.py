from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Brand
# Create your views here.

def product_list(request, category_slug=None):
    category = None
    brand = None
    categories = Category.objects.all()
    brands = Brand.objects.all()

    products = Product.objects.filter(available=True)
    if category_slug:
        category = Category.objects.filter(slug = category_slug)
        brand = Brand.objects.filter(slug = category_slug)
        if len(category) != 0:
            products = products.filter(category=category[0])
        else:
            products = products.filter(brand=brand[0])

    print(products)
    return render(request,
                  'products.html',
                  {'category': category,
                   'brand': brand,
                   'categories': categories,
                   'brands':brands,
                   'products': products})


# def product_list_brand(request, brand_slug=None):
#     category = None
#     brand = None
#     categories = Category.objects.all()
#     brands = Brand.objects.all()
#
#     products = Product.objects.filter(available=True)
#     if brand_slug:
#         brand = get_object_or_404(Brand, slug=brand_slug)
#         products = products.filter(brand=brand)
#
#     return render(request,
#                   'products.html',
#                   {'category': category,
#                    'brand': brand,
#                    'categories': categories,
#                    'brands': brands,
#                    'products': products})