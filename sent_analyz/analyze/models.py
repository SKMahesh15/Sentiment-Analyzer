from django.db import models

# Create your models here.
class Links(models.Model):
    link = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.link