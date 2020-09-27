# Generated by Django 3.1.1 on 2020-09-27 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctrl', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmpt_detail',
            name='count_all',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cmpt_detail',
            name='count_case',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cmpt_detail',
            name='count_cpu',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cmpt_detail',
            name='count_gpu',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cmpt_detail',
            name='count_hdd',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cmpt_detail',
            name='count_monitor',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cmpt_detail',
            name='count_program',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cmpt_detail',
            name='count_psu',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cmpt_detail',
            name='count_ram',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cmpt_detail',
            name='count_ssd',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cmpt_detail',
            name='count_windows',
            field=models.IntegerField(default=0),
        ),
    ]