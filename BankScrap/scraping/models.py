from django.db import models

# Create your models here.


class Stats(models.Model):
    name = models.CharField(max_length=120, verbose_name="Nazwa waloru")
    code = models.CharField(max_length=20, verbose_name="Kod waloru")
    price = models.CharField(max_length=20, verbose_name="Kurs")
    date = models.CharField(max_length=20, verbose_name="data i czas pobrania")

    class Meta:
        verbose_name_plural = "Stats"

    def __str__(self):
        return f"{self.name} {self.code} {self.price} {self.date}"