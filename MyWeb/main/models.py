from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', null=True, blank=True)

    def __str__(self):
        return self.title

class AboutMe(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name