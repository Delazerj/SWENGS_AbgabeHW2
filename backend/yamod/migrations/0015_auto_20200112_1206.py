# Generated by Django 2.2.7 on 2020-01-12 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yamod', '0014_auto_20200112_1017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='concert',
            old_name='artists',
            new_name='artist',
        ),
    ]