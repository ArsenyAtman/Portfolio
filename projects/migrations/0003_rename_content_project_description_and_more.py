# Generated by Django 4.1.3 on 2022-11-14 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_preview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='content',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='author',
        ),
        migrations.RemoveField(
            model_name='project',
            name='status',
        ),
        migrations.RemoveField(
            model_name='project',
            name='updated_on',
        ),
    ]
