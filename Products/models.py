from django.db import models

from datetime import datetime

class Products_List(models.Model):
    product_name = models.CharField(max_length=200, null=True)
    product_price = models.IntegerField(null=True)
    product_status = models.BooleanField(default=False, null=True)
    product_datestamp = models.DateTimeField(default=datetime.now(), null=True)
    
    def __str__(self):
        return self.product_name
    