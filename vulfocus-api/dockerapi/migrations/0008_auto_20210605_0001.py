# Generated by Django 3.1.4 on 2021-06-05 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dockerapi', '0007_auto_20210604_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timemoudel',
            name='time_id',
            field=models.CharField(default='05ce8a4e-90c0-4422-9447-3ece7ebe8fd0', max_length=255, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
