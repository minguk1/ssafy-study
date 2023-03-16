from django.db import models

# Create your models here.
class Article(models.Model):
    titile = models.CharField(max_length=20)
    content = models.TextField()