# Generated by Django 2.2.5 on 2019-10-22 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
