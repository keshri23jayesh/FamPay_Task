# Generated by Django 3.1.1 on 2020-09-03 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_server_calls', '0003_video_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video_details',
            name='publishedAt',
            field=models.CharField(max_length=50),
        ),
    ]
