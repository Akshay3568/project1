# Generated by Django 5.1.4 on 2025-02-08 08:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campapp', '0011_quizresult_course_description_alter_question_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('duration', models.IntegerField(help_text='Duration in years')),
                ('fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='campapp.college')),
            ],
        ),
    ]
