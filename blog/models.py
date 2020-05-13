from django.db import models
from datetime import datetime
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/blog/%Y/%m/%d/', blank=True)
    summary = models.TextField(max_length = 200)
    list_date = models.DateField(default=datetime.now)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    