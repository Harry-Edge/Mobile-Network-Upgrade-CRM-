# Generated by Django 3.1.2 on 2020-10-28 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20201028_1845'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mobilenumber',
            old_name='sms_sent',
            new_name='mms_sent',
        ),
    ]