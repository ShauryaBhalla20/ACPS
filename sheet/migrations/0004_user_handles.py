# Generated by Django 4.0.5 on 2024-05-15 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0003_alter_problem_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_handles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handle', models.CharField(max_length=100)),
            ],
        ),
    ]