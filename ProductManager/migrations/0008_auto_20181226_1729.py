# Generated by Django 2.0.7 on 2018-12-26 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductManager', '0007_auto_20181226_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(null=True, upload_to='media/products/cover'),
        ),
    ]
