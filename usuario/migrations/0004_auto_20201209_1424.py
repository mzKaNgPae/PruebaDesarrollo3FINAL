# Generated by Django 3.1.2 on 2020-12-09 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_auto_20201209_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipo_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipo', to='usuario.tipousuario'),
        ),
    ]
