# Generated by Django 3.1.1 on 2021-05-04 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210504_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.IntegerField()),
                ('otp', models.CharField(max_length=4)),
                ('is_verfied', models.BooleanField(default=False)),
            ],
        ),
    ]
