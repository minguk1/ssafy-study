# Generated by Django 3.2.18 on 2023-05-18 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='genres_id',
            new_name='genre_ids',
        ),
    ]
