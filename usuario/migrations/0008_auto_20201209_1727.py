# Generated by Django 3.1.2 on 2020-12-09 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0007_usuario_imagen_auto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='apellido_materno',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
