# Generated by Django 3.0.7 on 2020-06-13 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0004_auto_20200613_1216'),
        ('auth', '0011_update_proxy_permissions'),
        ('core', '0002_auto_20200613_1216'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]