# Generated by Django 4.2.16 on 2024-11-25 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lab6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('func1', models.CharField(max_length=255)),
                ('x1_0', models.FloatField()),
                ('y1_0', models.FloatField()),
                ('b1', models.FloatField()),
                ('x1_res', models.CharField(max_length=1024)),
                ('y1_res', models.CharField(max_length=1024)),
                ('func2', models.CharField(max_length=255)),
                ('x2_0', models.FloatField()),
                ('y2_0', models.FloatField()),
                ('b2', models.FloatField()),
                ('x2_res', models.CharField(max_length=1024)),
                ('y2_res', models.CharField(max_length=1024)),
            ],
        ),
    ]