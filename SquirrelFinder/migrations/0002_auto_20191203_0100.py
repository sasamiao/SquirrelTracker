# Generated by Django 2.2.7 on 2019-12-03 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SquirrelFinder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirreltracker',
            name='X',
            field=models.CharField(help_text='Latitude', max_length=50),
        ),
        migrations.AlterField(
            model_name='squirreltracker',
            name='Y',
            field=models.CharField(help_text='Longitude', max_length=50),
        ),
    ]
