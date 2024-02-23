from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_category = models.CharField(max_length=50)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_manufacturing_date = models.DateField()
    product_manufactured_by = models.CharField(max_length=100)

