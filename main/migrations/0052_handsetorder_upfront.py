# Generated by Django 3.1.2 on 2020-11-24 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0051_auto_20201124_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='handsetorder',
            name='upfront',
            field=models.FloatField(null=True),
        ),
    ]