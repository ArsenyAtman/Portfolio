# Generated by Django 4.1.3 on 2022-11-12 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='preview',
            field=models.ImageField(default=0, upload_to='images/'),
            preserve_default=False,
        ),
    ]