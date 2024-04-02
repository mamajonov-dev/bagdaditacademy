from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

class Teacher(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    # id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.name

