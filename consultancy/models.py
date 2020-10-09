from django.db import models


class paymentDetails(models.Model):
    fName = models.CharField(max_length=255)
    lName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=20)
    AccNo = models.CharField(max_length=10)
    tariff = models.CharField(max_length=10)
    unitMon1 = models.IntegerField()
    unitMon2 = models.IntegerField()
    unitMon3 = models.IntegerField()
    supMon1 = models.CharField(max_length=20)
    supMon2 = models.CharField(max_length=20)
    supMon3 = models.CharField(max_length=20)



class cusStatus(models.Model):
    cusName = models.CharField(max_length=255)
    projDetails = models.CharField(max_length=20000)
    location = models.CharField(max_length=100)
    totPrice = models.FloatField()


class cusDetails(models.Model):
    cusName = models.CharField(max_length=255)
    projDetails = models.CharField(max_length=20000)
    location = models.CharField(max_length=100)
    totPrice = models.FloatField()
    stageOnePrice = models.FloatField()
    stageTwoPrice = models.FloatField()
    stageThreePrice = models.FloatField()



