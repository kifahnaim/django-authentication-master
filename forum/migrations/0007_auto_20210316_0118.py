# Generated by Django 3.0.5 on 2021-03-15 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_auto_20210316_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]