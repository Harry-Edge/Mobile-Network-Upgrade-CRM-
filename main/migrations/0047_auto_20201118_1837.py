# Generated by Django 3.1.2 on 2020-11-18 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_auto_20201118_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='handsets',
            name='tariffs_availible',
            field=models.ManyToManyField(null=True, to='main.HandsetTariffs'),
        ),
        migrations.AddField(
            model_name='handsettariffs',
            name='contract_length',
            field=models.CharField(choices=[('24', '24')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='handsettariffs',
            name='data_allowance',
            field=models.CharField(choices=[('0.25', '0.25'), ('1', '1'), ('4', '4'), ('10', '10'), ('40', '40'), ('100', '100'), ('1000', '1000')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='handsettariffs',
            name='mrc',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='handsettariffs',
            name='plan_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='handsettariffs',
            name='plan_type',
            field=models.CharField(choices=[('Essential', 'Essential'), ('Smart', 'Smart')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='handsettariffs',
            name='tariff_code',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='handsettariffs',
            name='upfront',
            field=models.FloatField(null=True),
        ),
    ]
