# Generated by Django 3.0.5 on 2021-03-13 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userreg',
            old_name='thumbnail',
            new_name='user_thumbnail',
        ),
    ]