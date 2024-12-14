# Generated by Django 5.1.4 on 2024-12-13 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tayyabportfolio', '0003_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='skills/')),
                ('percentage', models.IntegerField()),
            ],
        ),
    ]