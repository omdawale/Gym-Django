# Generated by Django 3.1.6 on 2021-03-17 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0004_homefields_spanheading'),
    ]

    operations = [
        migrations.AddField(
            model_name='homefields',
            name='div2',
            field=models.CharField(default='Recent Post', max_length=100),
            preserve_default=False,
        ),
    ]
