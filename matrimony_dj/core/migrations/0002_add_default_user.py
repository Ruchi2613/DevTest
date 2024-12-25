# Generated by Django 4.2.17 on 2024-12-25 07:27

from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_default_user(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.create(
        username='Tom',
        email='Tom@example.com',
        password=make_password('toor1234')
    )

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),  # Ensure this matches the initial migration
    ]

    operations = [
        migrations.RunPython(create_default_user),
    ]