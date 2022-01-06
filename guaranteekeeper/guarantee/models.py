from django.db import models


class TimeStamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Guarantee(TimeStamped):
    product = models.CharField(max_length=30)
    model_code = models.CharField(max_length=30, blank=True)
    serial_number = models.CharField(max_length=40, blank=True, default='-')
    purchased_date = models.DateTimeField(blank=True, null=True)
    paid_money = models.IntegerField(blank=True, null=True)
    warranty = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.product

    class Meta:
        db_table = 'guarantee_information'
