from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.name
