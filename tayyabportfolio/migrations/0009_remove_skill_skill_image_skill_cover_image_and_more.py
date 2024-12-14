# Generated by Django 5.1.4 on 2024-12-14 13:49

import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tayyabportfolio', '0008_remove_skill_image_skill_skill_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='skill_image',
        ),
        migrations.AddField(
            model_name='skill',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='skills/images/'),
        ),
        migrations.AddField(
            model_name='skill',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skill',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='percentage',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
