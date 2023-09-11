from django.db import models

# Coffee bean model
class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    taste = models.TextField()
    