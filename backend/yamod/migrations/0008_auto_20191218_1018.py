# Generated by Django 2.2.7 on 2019-12-18 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yamod', '0007_auto_20191218_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ManyToManyField(blank=True, to='yamod.Album'),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ManyToManyField(blank=True, to='yamod.Artist'),
        ),
    ]
