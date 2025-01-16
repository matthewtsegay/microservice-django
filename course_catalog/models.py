from django.db import models
from django.contrib.auth import get_user_model
from users.models import User
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    available_slots = models.IntegerField(default=0)

    def __str__(self):
        return self.name


