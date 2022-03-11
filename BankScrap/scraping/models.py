from django.db import models

# All records from scraping are str so that's why is only CharField models.


class Stats(models.Model):
    name = models.CharField(max_length=120, verbose_name="Nazwa waloru")
    code = models.CharField(max_length=20, verbose_name="Kod waloru")
    price = models.CharField(max_length=20, verbose_name="Kurs")
    date = models.CharField(max_length=20, verbose_name="data i czas pobrania")

# Meta is for change name from django's Statss to Stats

    class Meta:
        verbose_name_plural = "Stats"

    def __str__(self):
        return f"{self.name} {self.code} {self.price} {self.date}"