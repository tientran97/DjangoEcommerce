
from django.shortcuts import render
from category.models import Category

from store.models import Product


def home(request):
    products = Product.objects.all().filter(is_available=True)
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request,'home.html', context)
