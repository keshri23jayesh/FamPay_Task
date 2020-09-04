# Generated by Django 3.1.1 on 2020-09-02 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_server_calls', '0002_auto_20200902_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='video_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=50, unique=True)),
                ('publishedAt', models.TextField()),
                ('video_title', models.TextField(blank=True)),
                ('video_desc', models.TextField(blank=True)),
                ('thumbnail_url', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'VIDEO_DETAILS',
            },
        ),
    ]
