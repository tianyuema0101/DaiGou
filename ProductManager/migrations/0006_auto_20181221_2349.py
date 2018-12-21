# Generated by Django 2.0.7 on 2018-12-21 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProductManager', '0005_auto_20181221_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='English_name',
            field=models.CharField(default='English Name', max_length=50),
        ),
        migrations.AddField(
            model_name='category',
            name='English_name',
            field=models.CharField(default='English Name', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='English_name',
            field=models.CharField(default='English Name', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='ProductManager.Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
    ]