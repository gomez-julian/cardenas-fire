from django.db import models

# Create your models here.

class PhotographicReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    app_title = models.CharField(max_length=50)
    date = models.DateField()


class PhotographicItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.TextField(max_length=250)
    pictureOne = models.CharField(max_length=100)
    pictureTwo = models.CharField(max_length=100)
    fk_informe = models.ForeignKey(PhotographicReport, on_delete=models.CASCADE)