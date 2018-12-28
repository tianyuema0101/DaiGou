from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Brand
# Create your views here.

def product_list(request, both_slug=None):
    category = None
    brand = None
    categories = Category.objects.all()
    brands = Brand.objects.all()

    products = Product.objects.filter(available=True)
    if both_slug:
        category = Category.objects.filter(slug = both_slug)
        brand = Brand.objects.filter(slug = both_slug)
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

def search_product(request):
    ##other error make the print go up 
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxcl")
    print(request.GET)
    category = None
    brand = None
    input_value = request.GET.get('search_input')
    selected_category = request.GET.get('selected_category')
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    brands = Brand.objects.all()

    return render(request,
                  'products.html',
                  {'category': category,
                   'brand': brand,
                   'categories': categories,
                   'brands':brands,
                   'products': products})