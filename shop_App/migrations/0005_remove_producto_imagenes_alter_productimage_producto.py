# Generated by Django 4.1.7 on 2023-03-10 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_App', '0004_comentario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='Imagenes',
        ),
        migrations.AlterField(
            model_name='productimage',
            name='Producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop_App.producto'),
        ),
    ]
