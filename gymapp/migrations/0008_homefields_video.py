# Generated by Django 3.1.6 on 2021-03-17 18:20

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0007_auto_20210317_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='homefields',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True),
        ),
    ]
