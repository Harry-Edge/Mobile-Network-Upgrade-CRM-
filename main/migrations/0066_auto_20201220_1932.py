# Generated by Django 3.1.2 on 2020-12-20 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0065_handsetorder_ctn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mobilenumber',
            name='annual_upgrade',
        ),
        migrations.RemoveField(
            model_name='mobilenumber',
            name='annual_upgrade_fee',
        ),
    ]