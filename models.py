from django.db import models
#from django.contrib.auth.models import User

class Employee(models.Model):
    ename_f = models.CharField(max_length=50)
    ename_l = models.CharField(max_length=50)
    econtact = models.CharField(max_length=10)
    egender = models.CharField(max_length=20)
    ehometown = models.CharField(max_length=20)

class Time(models.Model):
    ename_f = models.CharField(max_length=50)
    ename_l = models.CharField(max_length=50)
    eIntime = models.CharField(max_length=10)
    eOuttime = models.CharField(max_length=20)
    eOtherinfo = models.CharField(max_length=20)





