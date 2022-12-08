from django.db import models

from carService.models.Service import Service


class ServiceExtraLabor(models.Model):
    laborName = models.CharField(max_length=100, null=True, blank=True)
    laborPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    laborTaxRate = models.DecimalField(max_digits=10, decimal_places=2)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
