# Generated by Django 2.1.5 on 2019-06-20 05:57

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rango', '0004_userprofiles'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfiles',
            new_name='UserProfile',
        ),
    ]
