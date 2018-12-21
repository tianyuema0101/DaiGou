from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    English_name = models.CharField(max_length=50, default="English Name")
    slug = models.SlugField(max_length=200,
                            db_index=True,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])

class Brand(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    English_name = models.CharField(max_length=50, default="English Name")
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('ProductManager:product_list_by_brand',
                       args=[self.slug])

class Product(models.Model):
    auto_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="Not Created")
    English_name = models.CharField(max_length=50, default="English Name")
    slug = models.SlugField(max_length=200, db_index=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to='img/product', null=True)
    size = models.CharField(max_length=200, null=True)
    quantity = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    create_date = models.DateTimeField(auto_now_add=True)
    upload_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='img', null=True)

