# Generated by Django 5.0 on 2024-06-02 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otptoken',
            name='otp_code',
            field=models.CharField(default='101774', max_length=6),
        ),
    ]
