from django.db import models

from users.models import User
class ProductCategory(models.Model):
    name = models.CharField(max_length=128, null=False, unique=True)
    description = models.TextField(max_length=512, blank=True)
    
    class Meta:
        verbose_name_plural = 'Product Categories'

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256, null=False)
    image = models.ImageField(upload_to='products_images', blank=True)
    description = models.TextField(max_length=512, blank=True)
    short_description = models.CharField(max_length=64, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    quantity = models.PositiveBigIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self) -> str:
        readable_object =  f'Название: {self.name}, находится в категории: {self.category.name}'
        return readable_object


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f'Корзина для {self.user.username} | Продукт: {self.product.name}' 
    

    def amount(self):
        return self.quantity * self.product.price
    

    