# Generated by Django 3.1.2 on 2020-12-09 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0003_remove_auto_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='anno',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='auto',
            name='descripcion',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='auto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='auto',
            name='velocidad_maxima',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='auto',
            name='velocidad_partida',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
