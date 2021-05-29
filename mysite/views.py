from django.shortcuts import render
from django.http import HttpResponse
from mysite.models import Product
import random
# Create your views here.


def about(request):
    quotes = ['今日事，今日畢',
    '要怎麼收穫，先那麼栽',
    '知識就是力量',
    '一個人的個性就是他的命運']
    quote = random.choice(quotes)
    return render(request, 'about.html', locals())

def listing(request):
    products = Product.objects.all().order_by("-price").exclude(qty=0)
    products2 = Product.objects.filter(qty=0)
    return render(request, 'list.html', locals())


