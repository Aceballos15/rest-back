# Generated by Django 4.1.7 on 2023-04-14 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_remove_usuario_contrasena'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Documento',
            field=models.BigIntegerField(unique=True),
        ),
    ]
