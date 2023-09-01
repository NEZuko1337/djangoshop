from django.shortcuts import render, redirect, HttpResponse
from . models import *

from django.contrib.auth.decorators import login_required
# Рендер главной странички
def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', context)

# Рендер страницы с товарами на сайте
def products(request, category_id=None):
    # Trying to parse links for images
    # listwithurls = ['https://www.asos.com/au/adidas-originals/adidas-originals-monogram-hoodie-in-black/prd/22350203?colourwayid=60391872&cid=29259',
    #                 'https://www.farfetch.com/kz/shopping/men/the-north-face--item-18894294.aspx',
    #                 'https://www.asos.com/asos-design/asos-design-oversized-track-top-in-brown-teddy-borg/prd/21191840?colourwayid=60146970&cid=28239',
    #                 'https://www.slamdunk.su/product/view/12485',
    #                 'https://www.asos.com/es/dr-martens/zapatos-negros-con-plataforma-y-3-ojales-1461-bex-de-dr-martens/prd/9981067?clr=negro&colourwayid=15084628&SearchQuery=&cid=27116',
    #                 'https://needee.ru/p/ukorochennye-bryuki-strogogo-kroja-1331392690',
    # ]
    # main function
    categories = ProductCategory.objects.all()
    if category_id is not None:
        return render(request, 'products/products.html', {'categories' : categories, 'title': 'Store', 
        'products': Product.objects.filter(category_id=category_id),}) #'array' : listwithurls
    else:
        return render(request, 'products/products.html', {'categories' : categories, 'title': 'Store', 'products': Product.objects.all()},) #'array' : listwithurls

        

#Функция для добавления продукта в корзину
@login_required
def basket_add(request, product_id):
    CURRENT_PAGE = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user = request.user, product = product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return redirect(CURRENT_PAGE)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return redirect(CURRENT_PAGE)
    

#Функция для удаления продуктов
@login_required
def basket_remove(request, product_id):
    CURRENT_PAGE = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user = request.user, product = product)
    baskets.delete()
    return redirect(CURRENT_PAGE)


#Че нибудь можно придумать
@login_required
def confirm_order(request):
    return HttpResponse('<h1>Возможно, когда нибудь я это доделаю</h1>')
    