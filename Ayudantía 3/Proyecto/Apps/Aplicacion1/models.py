from django.db import models

# Create your models here.
class Fact(models.Model):
    fact_text = models.TextField()  # Campo para almacenar el texto del fact
    length = models.IntegerField()  # Campo para almacenar el número de length

    def __str__(self):
        return self.fact_text