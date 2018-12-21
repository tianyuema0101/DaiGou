# Generated by Django 2.0.7 on 2018-12-21 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductManager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='upload_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
