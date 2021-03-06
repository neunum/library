# Generated by Django 2.1.7 on 2019-03-27 14:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=256)),
                ('education', models.IntegerField(blank=True, choices=[(0, 'none'), (1, 'basic'), (2, 'vocational'), (3, 'secondary'), (4, 'higher')], null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('date_birth', models.DateField(blank=True, null=True)),
                ('hash', models.TextField(blank=True, null=True)),
                ('hash_valid_to', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
