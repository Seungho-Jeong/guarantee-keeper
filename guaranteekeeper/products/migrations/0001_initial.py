# Generated by Django 3.2 on 2022-02-19 17:32

from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeStampedModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.timestampedmodel')),
                ('category', models.CharField(choices=[('mobile', '모바일/웨어러블'), ('home', '가전제품'), ('pc', 'PC/노트북'), ('office', '사무용품')], max_length=6)),
                ('name', models.CharField(max_length=30)),
                ('model_code', models.CharField(blank=True, max_length=30)),
                ('serial_number', models.CharField(blank=True, max_length=40)),
                ('purchased_date', models.DateTimeField(blank=True, null=True)),
                ('purchased_money', models.IntegerField(default=0)),
                ('warranty_period', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('url_product', models.URLField(blank=True, max_length=60)),
                ('url_community', models.URLField(blank=True, max_length=60)),
                ('image_guarantee', models.ImageField(upload_to=products.models.get_image_upload_path)),
                ('image_product', models.ImageField(blank=True, null=True, upload_to=products.models.get_image_upload_path)),
                ('image_receipt', models.ImageField(blank=True, null=True, upload_to=products.models.get_image_upload_path)),
            ],
            options={
                'db_table': 'products',
            },
            bases=('products.timestampedmodel',),
        ),
    ]
