# Generated by Django 5.0.7 on 2024-07-30 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='sections',
            new_name='section',
        ),
    ]
