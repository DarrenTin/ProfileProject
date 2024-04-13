from django.db import models

# Create your models here.
class Identity(models.Model):
    attribute = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.attribute} {self.value}"
    
class Level(models.Model):
    skill = models.CharField(max_length=30)
    percentage = models.IntegerField()

    def __str__(self):
        return self.skill
    
class Fact(models.Model):
    fact = models.CharField(max_length=30)
    number = models.IntegerField()
    def __str__(self):
        return self.fact