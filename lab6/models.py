from django.db import models


class Lab6(models.Model):
    name = models.CharField(max_length=255, unique=True)

    # Task 1 related fields. Note that a is omitted since x0 copies its value
    func1 = models.CharField(max_length=255)
    x1_0 = models.FloatField()
    y1_0 = models.FloatField()
    b1 = models.FloatField()

    # Task 2 related fields
    func2 = models.CharField(max_length=255)
    x2_0 = models.FloatField()
    y2_0 = models.FloatField()
    b2 = models.FloatField()
