# Generated by Django 3.1.2 on 2020-10-28 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_mobilenumber_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='dob',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='first_line_address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='postcode',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
