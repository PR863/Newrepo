from django.db import models

# Create your models here.
class Custumor(models.Model):
    c_id = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    bill = models.FloatField()
