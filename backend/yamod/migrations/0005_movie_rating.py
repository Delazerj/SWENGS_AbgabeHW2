# Generated by Django 2.2.7 on 2019-12-11 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yamod', '0004_auto_20191126_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.PositiveIntegerField(default=0),
        ),
    ]