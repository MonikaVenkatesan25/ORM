from django.db import models
from django.contrib import admin
class shop(models.Model):
    customer_name=models.CharField(max_length=25)
    customer_id=models.IntegerField(primary_key=True)
    data_purchase=models.DateField()
    brand=models.CharField(max_length=20)
    payment_mode=models.CharField(max_length=30)

class shopAdmin(admin.ModelAdmin):
    list_display=["customer_name","customer_id","data_purchase","brand","payment_mode"]   
