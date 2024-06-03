# Generated by Django 5.0.6 on 2024-06-03 06:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_site', '0009_alter_product_discount_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SubCategory', to='shop_site.subcategory', verbose_name='subcategory'),
        ),
    ]