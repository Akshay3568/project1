# Generated by Django 5.1.4 on 2025-01-07 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=20),
        ),
    ]
