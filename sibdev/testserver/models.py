from django.db import models


# Create your models here.
class Deal(models.Model):
    id = models.IntegerField(primary_key=True)
    customer = models.TextField()
    item = models.TextField()
    total = models.IntegerField()
    quantity = models.IntegerField()
    date = models.TextField()

    def __str__(self):
        return self.item
