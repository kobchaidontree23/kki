# Generated by Django 3.2.5 on 2021-07-29 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_post_position'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='position',
            new_name='pos',
        ),
    ]
