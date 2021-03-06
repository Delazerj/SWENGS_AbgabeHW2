# Generated by Django 2.2.7 on 2019-12-18 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yamod', '0010_auto_20191218_1107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ManyToManyField(blank=True, to='yamod.Album'),
        ),
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.ManyToManyField(blank=True, to='yamod.Artist'),
        ),
    ]
