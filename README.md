# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).





## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py
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

admin.py
from django.contrib import admin
from .models import shop,shopAdmin
admin.site.register(shop,shopAdmin)



```


## OUTPUT

![alt text](<Screenshot (14).png>)


## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
