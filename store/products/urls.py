from django.contrib import admin
from django.urls import path, include
from products import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'products'

urlpatterns = [
    path('', views.products, name = 'home' ),
    path('<int:category_id>', views.products, name = 'category' ),
    path('basket-add/<int:product_id>',views.basket_add, name = 'basket_add'),
    path('basket-remove/<int:product_id>', views.basket_remove, name ='basket_remove'),
    path('confirm-order', views.confirm_order, name='confirm_order')
]