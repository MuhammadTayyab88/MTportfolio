from django.db import models

class Skills(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    cover_image = models.ImageField("skills/images/", blank=True, null=True)
    percentage = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"

class CV(models.Model):
    file = models.FileField(upload_to='cvs/')

class Profile(models.Model):
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
