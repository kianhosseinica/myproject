from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
class ShopInfo(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    hours = models.CharField(max_length=100)
    return_policy = models.TextField()
    shipping_info = models.TextField()
    special_offers = models.TextField()

    def __str__(self):
        return self.name