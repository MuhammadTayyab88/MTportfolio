# Generated by Django 5.1.4 on 2024-12-14 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tayyabportfolio', '0005_alter_skill_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='image',
            field=models.ImageField(default='skills/default.png', upload_to='skills/'),
        ),
    ]
