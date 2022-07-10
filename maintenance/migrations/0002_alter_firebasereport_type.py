# Generated by Django 4.0.4 on 2022-05-13 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firebasereport',
            name='type',
            field=models.CharField(choices=[('MS', 'Mensual'), ('TR', 'Trimestral'), ('AN', 'ANUAL')], default='MS', max_length=10),
        ),
    ]