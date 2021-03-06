# Generated by Django 3.2 on 2021-04-24 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CentralAudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('situacao', models.IntegerField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Consoles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('situacao', models.IntegerField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Diversos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('situacao', models.IntegerField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Ems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('situacao', models.IntegerField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Par2000T',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('situacao', models.IntegerField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Radios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('situacao', models.IntegerField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Telefonia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('situacao', models.IntegerField(max_length=1)),
            ],
        ),
    ]
