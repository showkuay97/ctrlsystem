# Generated by Django 3.1.1 on 2020-09-13 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctrl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='options_std',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_room', models.CharField(max_length=3)),
                ('slug_class_room', models.SlugField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='options_tcher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=255)),
                ('slug_room', models.SlugField(max_length=255)),
            ],
        ),
    ]
