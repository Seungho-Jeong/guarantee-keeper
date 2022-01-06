# Generated by Django 3.2 on 2022-01-05 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guarantee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.CharField(max_length=30)),
                ('model_code', models.CharField(blank=True, max_length=30)),
                ('serial_number', models.CharField(blank=True, max_length=40)),
                ('purchased_date', models.DateTimeField(blank=True, null=True)),
                ('paid_money', models.IntegerField(blank=True, null=True)),
                ('warranty', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'guarantee_information',
            },
        ),
    ]