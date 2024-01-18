from datetime import datetime

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    timestamp = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.name}'
