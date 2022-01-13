from django.db import models
from django.core.exceptions import ValidationError


def get_image_upload_path(instance, filename):
    """
    이미지 파일인지 검증하고 확장자를 제한한 뒤
    객체와 이미지 이름으로 동적인 저장 경로를 생성해주는 함수입니다.

    Parameters
    ----------
    instance: instance
        검증할 모델 인스턴스(객체)
    filename: str
        이미지 파일의 이름

    Return
    ------
    path: dynamic path
        인스턴스 이름과 파일 이름을 조합한 동적인 미디어 파일 저장경로
    """

    try:
        image_extensions = ['jpg', 'jpeg', 'png', 'gif']
        if filename.split(".")[-1] not in image_extensions:
            raise ValidationError('`%s` is not a supported image extension. (support: jpg, jpeg, png, gif)' % filename)
        return f'media/{instance}/{filename}'

    except TypeError:
        raise ValidationError('`%s` is not a supported file extension.' % filename)


class TimeStamped(models.Model):
    """
    추가적으로 생성될 수 있는 모델에 반복적으로 사용될 필드인
    생성일시와 수정일시를 상속시키기 위하여 추상화한 모델 클래스입니다.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Guarantee(TimeStamped):
    """
    Guarantee keeper의 기본 인스턴스 모델입니다.
    카테고리는 중복 가능하며 2 Depth로 생성될 수 있으므로 추후 테이블 분리할 필요가 있습니다.
    """

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
