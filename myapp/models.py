from django.db import models

class Supplier(models.Model):
    eid = models.CharField(max_length=30)
    ename = models.CharField(max_length=100)
    sname = models.CharField(max_length=30)
    pname = models.CharField(max_length=30)
    sprice = models.FloatField()
    eemail = models.EmailField()
    econtact = models.CharField(max_length=30)



class Product(models.Model):
    pid = models.CharField(max_length=30)
    prname = models.CharField(max_length=100)
    price = models.FloatField()
    suname = models.CharField(max_length=30)
    scname = models.CharField(max_length=30)
    dis = models.CharField(max_length=30)


class Contract(models.Model):
    cid = models.CharField(max_length=30)
    cname = models.CharField(max_length=100)
    camount = models.FloatField()
    cproduct = models.CharField(max_length=30)
    sdate = models.CharField(max_length=30)
    edate = models.CharField(max_length=30)


class Rating(models.Model):
    vname = models.CharField(max_length=30)
    vproduct = models.CharField(max_length=30)
    quality = models.CharField(max_length=100)
    rdeli = models.CharField(max_length=30)
    rprice = models.CharField(max_length=30)
    service = models.CharField(max_length=30)
    risk = models.CharField(max_length=30)

