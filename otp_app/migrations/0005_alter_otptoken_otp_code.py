# Generated by Django 5.0 on 2024-06-12 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp_app', '0004_alter_otptoken_otp_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otptoken',
            name='otp_code',
            field=models.CharField(default='5b0a1a', max_length=6),
        ),
    ]