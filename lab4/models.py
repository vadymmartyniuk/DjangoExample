from django.db import models


class Lab4(models.Model):
    name = models.CharField(max_length=255, unique=True)

    # Integration results
    area1 = models.FloatField() # hold 3 float values, so its field type should be changed
    area2 = models.FloatField()
    area3 = models.FloatField()

    # Rectangle method
    a1 = models.FloatField()
    b1 = models.FloatField()
    n1 = models.PositiveIntegerField()
    func1 = models.CharField(max_length=255)

    # Simpson method
    a2 = models.FloatField()
    b2 = models.FloatField()
    n2 = models.PositiveIntegerField()
    func2 = models.CharField(max_length=255)

    # Trapezoid method
    a3 = models.FloatField()
    b3 = models.FloatField()
    n3 = models.PositiveIntegerField()
    func3 = models.CharField(max_length=255)

    def __str__(self):
        return self.name
