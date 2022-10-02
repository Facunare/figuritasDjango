
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class tipos_figus(models.Model):
    type = models.CharField(max_length=4)
   
    def __str__(self):
        return self.type

class figus_totales(models.Model):    
    figurita = models.CharField(max_length=50, primary_key = True)
    num_figu = models.IntegerField(default=0)
    type = models.ForeignKey(tipos_figus, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return str(self.type) + str(self.num_figu)

