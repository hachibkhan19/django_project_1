from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    des = models.TextField(max_length=500)
    img = models.ImageField(upload_to='picture')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    