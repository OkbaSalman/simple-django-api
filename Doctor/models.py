from django.db import models

class Doctor(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    speciality=models.CharField(max_length=20)
    phoneNumber=models.CharField(max_length=14)
    isAvailable= models.BooleanField(default=True)

    def __str__(self):
        return self.firstName + " " + self.lastName