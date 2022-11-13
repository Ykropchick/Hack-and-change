from django.db import models


class Streamers(models.Model):
    id = models.AutoField(primary_key=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name="Фото")
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name