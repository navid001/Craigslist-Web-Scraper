# Generated by Django 4.0 on 2022-03-14 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
