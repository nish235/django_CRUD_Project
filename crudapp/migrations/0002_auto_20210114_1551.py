# Generated by Django 3.1.4 on 2021-01-14 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='city',
            field=models.CharField(default='', editable=False, max_length=20),
        ),
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(default='', editable=False, max_length=100),
        ),
        migrations.AddField(
            model_name='member',
            name='mobile',
            field=models.CharField(default='', editable=False, max_length=12),
        ),
    ]
