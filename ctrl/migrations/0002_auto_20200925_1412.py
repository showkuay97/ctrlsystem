# Generated by Django 3.1.1 on 2020-09-25 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctrl', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repair_cmpt',
            name='date_input',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='repair_cmpt',
            name='date_output',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='repair_cmpt',
            name='date_report',
            field=models.DateField(),
        ),
    ]
