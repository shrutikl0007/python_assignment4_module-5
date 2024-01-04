from django.db import models

# Create your models here.


class Product(models.Model):
    Product_id = models.IntegerField()
    product_name = models.CharField(max_length=200)

    def __str__(self):
        return str( self.Product_id )  + (".") + ( self.product_name)  # for admin use
