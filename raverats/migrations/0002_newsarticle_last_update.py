# Generated by Django 3.2.13 on 2023-08-07 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
