from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Subdomain(models.Model):
    id = models.BigAutoField(primary_key=True)
    subdomain = models.CharField(max_length=3)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
