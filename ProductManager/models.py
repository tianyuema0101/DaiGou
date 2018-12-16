from django.db import models

# Create your models here.
class Product(models.Model):
    auto_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="Not Created")
    Type = models.CharField(max_length=50, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    create_date = models.DateTimeField(auto_now_add=True)
    upload_date = models.DateTimeField(auto_now_add=True)


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='img', null=True)
