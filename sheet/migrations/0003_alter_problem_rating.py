# Generated by Django 4.0.5 on 2024-05-13 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0002_problem_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='rating',
            field=models.IntegerField(default=800),
        ),
    ]
