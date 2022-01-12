from django.db import models
from django.core.exceptions import ValidationError


def get_image_upload_path(instance, filename):
    try:
        image_extensions = ['jpg', 'jpeg', 'png', 'gif']
        if filename.split(".")[-1] not in image_extensions:
            raise ValidationError('`%s` is not a supported image extension. (support: jpg, jpeg, png, gif)' % filename)
        return f'media/{instance}/{filename}'
    except TypeError:
        raise ValidationError('`%s` is not a supported file extension.' % filename)


class TimeStamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Guarantee(TimeStamped):
    CATEGORY_CHOICES = [
        ('mobile', '모바일/웨어러블'),
        ('home', '가전제품'),
        ('pc', 'PC/노트북'),
        ('office', '사무용품'),
    ]

    category = models.CharField(max_length=6, choices=CATEGORY_CHOICES)
    product = models.CharField(max_length=30)
    model_code = models.CharField(max_length=30, blank=True)
    serial_number = models.CharField(max_length=40, blank=True, default='-')
    purchased_date = models.DateTimeField(blank=True, null=True)
    paid_money = models.PositiveIntegerField(default=0)
    warranty = models.DateTimeField(blank=True, null=True)
    warranty_image = models.ImageField(upload_to=get_image_upload_path)
    product_image = models.ImageField(upload_to=get_image_upload_path, blank=True, null=True)
    receipt_image = models.ImageField(upload_to=get_image_upload_path, blank=True, null=True)

    def __str__(self):
        return self.product

    class Meta:
        db_table = 'guarantees'
