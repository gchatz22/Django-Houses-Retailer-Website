# Generated by Django 2.1.5 on 2019-01-13 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='bathrooms',
        ),
    ]
