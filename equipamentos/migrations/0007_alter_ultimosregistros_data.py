# Generated by Django 3.2 on 2021-04-29 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipamentos', '0006_auto_20210429_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ultimosregistros',
            name='data',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
