from django.db import models
from datetime import datetime
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Study(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/%Y/%m/%d/')

    def __str__(self):
        return self.title


class Entertainment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/%Y/%m/%d/')

    def __str__(self):
        return self.title

class Extra(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    files = models.FileField(upload_to='videos/%Y/%m/%d/')

    def __str__(self):
        return self.title