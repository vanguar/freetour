# Generated by Django 2.0.13 on 2019-03-14 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190314_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='travel_dates',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
