from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class VesetModel(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    ona = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}: {self.year}-{self.month}-{self.day} {self.ona}'
    