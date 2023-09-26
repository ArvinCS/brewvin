from django.contrib.auth.models import User
from django.db import models

# Coffee bean model
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    taste = models.TextField()