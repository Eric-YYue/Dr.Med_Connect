# Generated by Django 3.1 on 2021-05-08 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0005_auto_20210507_0016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prescription',
            options={'get_latest_by': 'id'},
        ),
    ]
