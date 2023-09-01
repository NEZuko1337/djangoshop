from django.shortcuts import render, redirect
from . forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from products.models import Basket

# Создание пользователя
def registeruser(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:loginuser')
        else:
            return render(request, 'users/register.html', {'form' : form})
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form' : form})


# Логин пользователя
def loginuser(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password = password) # authenticate and after login!!!
            if user and user.is_active: # or user is not None
                login(request, user)
                return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form':form})


# Функция редактирования и просмотра профиля + Корзина(да, да не удивляйтесь)
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data = request.POST, instance = request.user, files = request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
        else:
            return render(request, 'users/profile.html', {'form' : form, 'error' : 'Something went wrong'})
    else:
        form = UserProfileForm(instance=request.user)
    
    # Подсчет итогового количества товаров и итоговой суммы за них.
    baskets = Basket.objects.filter(user = request.user)
    total_quantity = sum(basket.quantity for basket in baskets)
    total_price = sum(basket.amount() for basket in baskets) # basket.amount() смотреть в products.models.py

    # Итоговый ретерн
    return render(request, 'users/profile.html', 
                  {'form' : form, 
                   'baskets' : baskets, 
                   'total_quantity' : total_quantity,  
                   'total_price' : total_price,
                   })


#Функция для выхода из своего профиля
@login_required
def logoutuser(request):
    logout(request)
    return redirect('home')