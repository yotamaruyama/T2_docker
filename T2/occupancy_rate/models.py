# models.py

from django.db import models

class MachineData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    is_operational = models.BooleanField(default=False)
