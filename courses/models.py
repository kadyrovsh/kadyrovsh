from django.db import models

class Yonalish(models.Model):
    name = models.CharField(max_length=30)
    start_date = models.DateField(blank=False)
    is_active = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class Ustoz(models.Model):
    ism = models.CharField(max_length=15, default=True)
    familiya = models.CharField(max_length=15)
    malumot = models.CharField(max_length=15)
    def __str__(self):
        return self.ism

class Fan(models.Model):
    nom = models.CharField(max_length=25)
    yonalish = models.ForeignKey(Yonalish, on_delete=models.CASCADE, blank=True)
    ustozlar = models.ManyToManyField(Ustoz, null=True)
    def __str__(self):
        return self.nom






