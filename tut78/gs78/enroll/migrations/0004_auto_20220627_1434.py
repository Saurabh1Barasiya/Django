# Generated by Django 3.0.2 on 2022-06-27 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0003_auto_20220627_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='tpass_date',
            field=models.DateField(default='10/20/2000'),
        ),
    ]