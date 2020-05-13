from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/projects/%Y/%m')
    is_published = models.BooleanField(default = True)
    code_url = models.CharField(max_length=300)

    def __str__(self):
        return self.title
    