# Generated by Django 3.1.2 on 2020-12-10 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0009_auto_20201210_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='descripcion',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='auto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='bd/autos'),
        ),
    ]