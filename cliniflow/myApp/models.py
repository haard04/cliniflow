from django.db import models

class Medication(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Disease(models.Model):
    name = models.CharField(max_length=100, unique=True)
    preset_medications = models.ManyToManyField(Medication, blank=True)

    def __str__(self):
        return self.name
