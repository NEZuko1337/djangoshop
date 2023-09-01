from django.contrib import admin
from django.urls import path, include
from products import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),  
    path('products/', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)