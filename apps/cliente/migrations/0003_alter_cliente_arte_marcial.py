# Generated by Django 4.2.3 on 2023-07-16 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_cliente_arte_marcial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='arte_marcial',
            field=models.CharField(max_length=50),
        ),
    ]
