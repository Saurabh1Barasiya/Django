# Generated by Django 3.0.2 on 2022-03-31 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='stu_comment',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='stu_email',
            field=models.EmailField(default=True, max_length=254),
        ),
    ]
