# Generated by Django 3.1.2 on 2020-11-08 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20201108_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spendcaps',
            name='cap_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
