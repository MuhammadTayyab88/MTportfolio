# Generated by Django 5.1.4 on 2024-12-14 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tayyabportfolio', '0004_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='percentage',
            field=models.PositiveIntegerField(),
        ),
    ]
