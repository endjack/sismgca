# Generated by Django 3.2 on 2021-04-29 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipamentos', '0009_par2000t_ultimos_registros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='par2000t',
            name='ultimos_registros',
            field=models.ManyToManyField(blank=True, to='equipamentos.UltimosRegistros'),
        ),
    ]
