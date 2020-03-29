from django.db import models

# Create your models here.
# Remember ORM consists of wrapping all rows loaded from the database into a series of models
# Models are Python objects that have attributes that correspond to columns in a database row
# NB: CharField maps to SQL type VARCHAR, IntegerField to Integers, BooleanField to booleans, etc.
class Product(models.Model):

    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    slug = models.SlugField(max_length=48)
    active = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    date_updated = models.DateTimeField(auto_now=True)


# Foreign key is a field that stores the primary key of the linked Product model.
# It's used by the ORM to run JOIN operations automatically when accessed
# NB: ImageField is a subclass of FileField, and it offers a few additional functionalities for uploaded images
# This extra function requires the Pillow Library.
class ProductImage(models.Model):

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="product-images")


class ProductTag(models.Model):
    products = models.ManyToManyField(Product, blank=True)
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=48)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to="product-thumbnails", null=True)