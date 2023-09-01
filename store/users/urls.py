from django.contrib import admin
from django.urls import path, include
from users import views
from django.conf.urls.static import static
app_name = 'users'

urlpatterns = [
    path('loginuser/', views.loginuser, name = 'loginuser' ),
    path('registeruser/', views.registeruser, name = 'registeruser' ),
    path('profile/', views.profile, name = 'profile'),
    path('logoutuser/', views.logoutuser, name = 'logoutuser')
]