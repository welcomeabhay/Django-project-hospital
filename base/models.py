from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=60)
    diagnostics = models.TextField()
    Location = models.CharField(max_length=60)
    Specialization = models.CharField(max_length=100, choices=(('ortho', 'ORTHO'), ('derma', 'DERMA')))

    def __str__(self):
        return self.name

class Doctor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    Specialization = models.CharField(max_length=100, choices=(('ortho', 'ORTHO'), ('derma', 'DERMA'),('gm','GM')))
    def __str__(self):
        return self.name
class Patient(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.TextField(max_length=200,null=True,blank=False)
    mobile = models.IntegerField(null=True,blank=False)

    def __str__(self):
        return self.name

class Patient_Records(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    diagnostics = models.TextField(blank=True)
    observations = models.TextField(blank=True)
    treatments = models.TextField(blank=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,default=None,blank=True,null=True)
    def __str__(self):
        return self.patient.name

