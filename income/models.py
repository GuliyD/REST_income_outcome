from django.db import models


class Income(models.Model):
    income = models.DecimalField(max_digits=100, decimal_places=2)
    data_and_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.income)


class Outcome(models.Model):
    outcome = models.DecimalField(max_digits=100, decimal_places=2)
    data_and_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.outcome)