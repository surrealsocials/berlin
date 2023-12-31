# Generated by Django 3.2.13 on 2023-08-07 14:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('title', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('subtitle', models.TextField()),
                ('tag', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
                ('url', models.TextField(default='#')),
                ('story', models.TextField(default='')),
            ],
        ),
    ]
