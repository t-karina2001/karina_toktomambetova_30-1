from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=64)


class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=128)
    price = models.FloatField()
    description = models.TextField()
    rate = models.FloatField()

    categories = models.ManyToManyField(Category)


