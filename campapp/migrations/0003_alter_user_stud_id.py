# Generated by Django 5.1.4 on 2025-01-07 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campapp', '0002_user_full_name_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='stud_id',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
    ]
