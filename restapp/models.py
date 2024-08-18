from django.db import models

# Create your models here.
class MenuItem(models.Model):
    title=models.CharField(max_length=20)
    price=models.IntegerField()
    inventory=models.SmallIntegerField()