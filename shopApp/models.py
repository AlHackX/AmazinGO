from django.db import models

# Create your models here.

class Product(models.Model):
    #Definir campos de la tabla
    product_name = models.CharField(max_length=100, unique=True)
    product_description = models.CharField(max_length=250)
    product_full_cost = models.DecimalField(max_digits=10, decimal_places=2)
    product_is_offer = models.BooleanField()
    product_offer_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(Self):
        return Self.product_name

class HistoricalCost(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    change_date = models.DateTimeField()
    product_cost = models.DecimalField(max_digits=10, decimal_places=2)
    product_is_offer = models.BooleanField()

    def __str__(Self):
        return Self.product.product_name + "" + Self.change_date.strftime('%Y-%m-%d %H:%M')
    
class Contacts(models.Model):
    #Definir campos de la tabla
    contact_full_name = models.CharField(max_length=100, unique=True)
    contact_address = models.CharField(max_length=250)
    contact_phone = models.CharField(max_length=30)
    contact_email = models.CharField(max_length=50)
    contact_active = models.BooleanField()

    def __str__(self):
        return self.contact_full_name