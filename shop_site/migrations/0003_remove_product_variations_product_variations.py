# Generated by Django 5.0.6 on 2024-06-02 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_site', '0002_alter_product_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='variations',
        ),
        migrations.AddField(
            model_name='product',
            name='variations',
            field=models.ManyToManyField(blank=True, null=True, to='shop_site.variations', verbose_name='variations'),
        ),
    ]