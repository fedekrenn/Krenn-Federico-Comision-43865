# Generated by Django 4.2.3 on 2023-08-12 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0008_restaurante_horario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurante',
            name='horario',
        ),
    ]
