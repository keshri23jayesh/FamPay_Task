# Generated by Django 3.1.1 on 2020-09-04 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_server_calls', '0006_auto_20200904_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='api_keys',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
