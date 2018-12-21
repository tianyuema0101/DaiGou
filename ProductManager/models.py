from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            db_index=True,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])

class Product(models.Model):
    auto_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="Not Created")
    category = models.ForeignKey(Category,
                                 related_name='products', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    create_date = models.DateTimeField(auto_now_add=True)
    upload_date = models.DateTimeField(auto_now=True)


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='img', null=True)

