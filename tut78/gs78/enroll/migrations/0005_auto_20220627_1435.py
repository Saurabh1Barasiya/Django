# Generated by Django 3.0.2 on 2022-06-27 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0004_auto_20220627_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='tpass_date',
            field=models.DateField(default='2000/01/01'),
        ),
    ]