# Generated by Django 4.1.1 on 2022-10-09 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicleapp', '0003_mechanic_userdetail_request'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetail',
            old_name='request',
            new_name='requested',
        ),
    ]
