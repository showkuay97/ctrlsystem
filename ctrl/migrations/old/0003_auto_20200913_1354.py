# Generated by Django 3.1.1 on 2020-09-13 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctrl', '0002_options_std_options_tcher'),
    ]

    operations = [
        migrations.AddField(
            model_name='repair_cmpt',
            name='date_report',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='repair_cmpt',
            name='date_input',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='repair_cmpt',
            name='date_output',
            field=models.DateField(auto_now=True),
        ),
    ]
