# Generated by Django 4.1.7 on 2023-04-12 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_usuario_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='Contrasena',
        ),
    ]
