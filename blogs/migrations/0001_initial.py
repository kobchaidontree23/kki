# Generated by Django 3.2.5 on 2021-07-24 17:35

from django.db import migrations, models
from django.db.models.fields import TextField


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                
            ],
        ),
    ]