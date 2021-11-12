from django.db import models

# Create your models here.

class Info(models.Model):
    data = models.DateField(auto_now=False)
    Milk=models.CharField(max_length=100,default='')
    PTM =models.CharField(max_length=100,default='')
    Other=models.CharField(max_length=100,default='')
    Case=models.CharField(max_length=100,default='')
    Duy =models.CharField(max_length=100,default='')
    Total =models.CharField(max_length=100,default='')

    


