# Generated by Django 2.1.5 on 2019-06-20 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='api_key',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='api_secret',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
