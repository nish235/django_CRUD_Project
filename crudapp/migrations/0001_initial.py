# Generated by Django 3.1.4 on 2021-01-14 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'blog_member',
            },
        ),
    ]
