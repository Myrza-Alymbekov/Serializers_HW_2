from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} - {self.department}'


class Employee(models.Model):
    name = models.CharField(max_length=30)
    birth_date = models.DateField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='employees')
    salary = models.IntegerField(default=0)

    def __str__(self):
        return self.name

