# Generated by Django 5.1.2 on 2024-11-14 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_project_link_project_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutme',
            name='bio',
        ),
    ]
