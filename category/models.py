from django.db import models

class Category(models.Model):
    categoryName = models.CharField(max_length=255)

    def __str__(self):
        return self.categoryName
    
    
