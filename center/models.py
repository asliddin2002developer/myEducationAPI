from django.db import models

# Create your models here.
class Center(models.Model):
    name=models.CharField(blank=True, max_length=355, null=True)
    description=models.TextField(blank=True, null=True)
    price=models.FloatField(blank=True, null=True)
    tags=models.TextField(blank=True, null=True)
    imageUrl=models.URLField(blank=True, null=True, max_length=355)
    optionName = models.CharField(max_length=355, blank=True, null=True)
    hidden = models.CharField(blank=True, null=True, max_length=355)
    weight = models.FloatField(blank=True, null=True)
    prepaymentPercent = models.FloatField(null=True, blank=True)
    hideBuyBtn = models.CharField(blank=True, null=True, max_length=355)
    bonusesPercent = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.name)    