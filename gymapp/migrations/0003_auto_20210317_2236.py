# Generated by Django 3.1.6 on 2021-03-17 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0002_homefields_heading1'),
    ]

    operations = [
        migrations.AddField(
            model_name='homefields',
            name='heading2',
            field=models.CharField(default='Get Into The Best Gym in India', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homefields',
            name='heading1',
            field=models.CharField(max_length=50),
        ),
    ]
