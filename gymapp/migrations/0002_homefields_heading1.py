# Generated by Django 3.1.6 on 2021-03-17 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homefields',
            name='heading1',
            field=models.CharField(default='Best Gym', max_length=100),
            preserve_default=False,
        ),
    ]