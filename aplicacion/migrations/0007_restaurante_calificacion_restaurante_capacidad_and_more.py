# Generated by Django 4.2.3 on 2023-08-12 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0006_cocinero_anios_experiencia_cocinero_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurante',
            name='calificacion',
            field=models.IntegerField(choices=[(1, 'A mejorar'), (2, 'Regular'), (3, 'Bueno'), (4, 'Muy bueno'), (5, 'Excelente')], default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurante',
            name='capacidad',
            field=models.IntegerField(default=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurante',
            name='envio_domilicio',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurante',
            name='eventos',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
