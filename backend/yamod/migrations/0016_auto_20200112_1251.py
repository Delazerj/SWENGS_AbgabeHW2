# Generated by Django 2.2.7 on 2020-01-12 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yamod', '0015_auto_20200112_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='artist',
            field=models.ManyToManyField(to='yamod.Artist'),
        ),
        migrations.AlterField(
            model_name='concert',
            name='begin_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='concert',
            name='end_date',
            field=models.DateField(null=True),
        ),
    ]
