from django.db import models
class destination(models.Model):
    name = models.CharField(max_length = 100)
    price = models.IntegerField()
    img = models.ImageField(upload_to = 'pics')