from django.db import models

class Employee(models.Model):
    ename_f = models.CharField(max_length=50)
    ename_l = models.CharField(max_length=50)
    econtact = models.CharField(max_length=10)
    egender = models.CharField(max_length=20)
    ehometown = models.CharField(max_length=20)






