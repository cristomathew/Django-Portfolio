from django.db import models
from datetime import datetime
# Create your models here.
categorychoices = {
  ('Entertainment', 'Entertainment'),
  ('Extra', 'Extra'),
  ('Study', 'Study'),
  }
filechoices = {
  ('pdf', 'pdf'),
  ('video', 'video'),
  ('docx', 'docx'),
  ('pic', 'pic'),
  ('other', 'other'),

  }
class Category(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(blank=True)
    typ= models.CharField(max_length=100,choices=categorychoices,default="Extra")
    def __str__(self):
        return self.title


class Study(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=100,choices=filechoices,default="video")
    video = models.FileField(upload_to='videos/%Y/%m/%d/')

    def __str__(self):
        return self.title


class Entertainment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=100,choices=filechoices,default="video")
    video = models.FileField(upload_to='videos/%Y/%m/%d/')

    def __str__(self):
        return self.title

class Extra(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=100,choices=filechoices,default="video")
    files = models.FileField(upload_to='videos/%Y/%m/%d/')

    def __str__(self):
        return self.title