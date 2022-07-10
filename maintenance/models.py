from django.db import models

# Create your models here.
class FirebaseReport(models.Model):
    CHOICES = [
        ('MS','Mensual'),
        ('TR','Trimestral'),
        ('AN','Anual')
    ]

    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    title = models.CharField(max_length=50)
    maintenance_worker = models.CharField(max_length=100)
    maintenance_engineer = models.CharField(max_length=100)
    contract = models.CharField(max_length=100)
    fire_network = models.CharField(max_length=100)
    contractor = models.CharField(max_length=100)
    contratista = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=CHOICES, default='MS')