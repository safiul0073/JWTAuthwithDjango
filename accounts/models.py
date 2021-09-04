from django.db import models

# Create your models here.

class Category(models.Model):
    STATUS = (
        ('Active','Active'),
        ('UnActive','UnActive')
    )
    title = models.CharField(max_length=200, null=True)
    slug = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=200, null=True)
    size = models.IntegerField(null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    images = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
       return self.name