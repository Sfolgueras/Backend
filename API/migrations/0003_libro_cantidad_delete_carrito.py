# Generated by Django 4.1.7 on 2023-05-12 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_alter_carrito_cantidad_alter_carrito_libro_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='cantidad',
            field=models.IntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='Carrito',
        ),
    ]
