# Generated by Django 3.0.5 on 2021-03-19 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20210313_1415'),
        ('forum', '0008_post_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='Post_likes', to='authapp.Userreg'),
        ),
    ]
