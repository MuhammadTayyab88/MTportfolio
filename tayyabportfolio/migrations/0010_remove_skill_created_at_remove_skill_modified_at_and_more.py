# Generated by Django 5.1.4 on 2024-12-14 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tayyabportfolio', '0009_remove_skill_skill_image_skill_cover_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='modified_at',
        ),
        migrations.AlterField(
            model_name='skill',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]