from django.db import models

# Create your models here.

class Directory (models.Model):
    last_name = models.CharField(null=False, max_length=20)
    first_name = models.CharField(null=False, max_length=20)
    other_name = models.CharField(null=True, max_length=20)
    tel = models.CharField(unique=True, max_length=11)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.first_name

