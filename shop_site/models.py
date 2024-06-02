from django.db import models

# Create your models here.


class MainCategory(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name="main category")

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    Main = models.ForeignKey(MainCategory, null=True, blank=True, on_delete=models.CASCADE, verbose_name="main category", related_name="MainCategory")
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name="subcategory")

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name="color")

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name="size")

    def __str__(self):
        return self.name


class Variations(models.Model):
    color = models.ForeignKey(Color, null=True, blank=True, on_delete=models.CASCADE, verbose_name="color", related_name="Color")
    size = models.ForeignKey(Size, null=True, blank=True, on_delete=models.CASCADE, verbose_name="size", related_name="Size")

    def __str__(self):
        return str(self.color) + " " + str(self.size)


class Product(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True, verbose_name="ProTiitle")
    description = models.TextField(blank=True, null=True, verbose_name="ProDescription")
    image = models.ImageField(blank=True, null=True, verbose_name="image")
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True, verbose_name="price")
    discount = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True, verbose_name="discount")
    quantity = models.IntegerField(default=0, blank=True, null=True, verbose_name="quantity")
    variations = models.ManyToManyField(Variations, blank=True, null=True, verbose_name="variations")

    def __str__(self):
        return self.title


