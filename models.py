from django.db import models
class Bank(models.Model):
    objects=models.Manager
    cid=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=20)
    gender=models.CharField(max_length=6)
    phno=models.IntegerField(max_length=10)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    uname=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
class Transactions(models.Model):
    objects=models.Manager
    cid=models.IntegerField()
    date=models.DateField()
    type=models.CharField(max_length=10)
    Amt=models.DecimalField(max_digits=10,decimal_places=2)