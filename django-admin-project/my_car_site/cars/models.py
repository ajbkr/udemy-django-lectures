from django.db import models  # noqa: F401


class Car(models.Model):
    brand = models.CharField(max_length=30)
    year = models.IntegerField()

    def __str__(self):
        return f'Car is {self.brand} {self.year}'
