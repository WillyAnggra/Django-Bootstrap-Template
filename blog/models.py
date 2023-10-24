from django.db import models
from category.models import Category

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    deskripsi = models.CharField(max_length=255)
    categoryName = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title 
