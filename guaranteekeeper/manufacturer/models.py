from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    address = models.CharField(max_length=120)


class Manufacturer(models.Model):
    name_ko = models.CharField(max_length=20)
    name_en = models.CharField(max_length=60)
    telephone = models.IntegerField(max_length=15)
    home_page = models.CharField(max_length=30)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
