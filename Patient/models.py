from django.db import models

# Create your models here.
class Patient(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    birthDate=models.DateField()
    phoneNumber=models.CharField(max_length=14)
    isInsured= models.BooleanField(default=False)