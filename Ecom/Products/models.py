from django.db import models

# Create your models here.
class Product(models.Model):
	title		= models.TextField()
	description	= models.CharField(max_length=100,null=True)
	Price		= models.DecimalField(decimal_places=2,max_digits=10000,null=False,default=0)