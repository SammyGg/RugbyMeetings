# Generated by Django 5.0.1 on 2024-03-11 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meeting',
            old_name='Room',
            new_name='room',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='floor_number',
            new_name='floor',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='Name',
            new_name='name',
        ),
    ]
