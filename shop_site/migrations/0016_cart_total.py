# Generated by Django 5.0.6 on 2024-06-06 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_site', '0015_cart_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='total'),
        ),
    ]