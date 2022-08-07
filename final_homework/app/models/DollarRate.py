from django.db import models


class DollarRate(models.Model):
    objects = models.Manager()
    dollar = models.DecimalField(null=False, default="0", max_digits=10, decimal_places=2)

    def __str__(self):
        return self.dollar
