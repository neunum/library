# Generated by Django 2.1.7 on 2019-03-27 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20190327_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='hash_valid_to',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
