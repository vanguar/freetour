# Generated by Django 2.1.7 on 2019-03-21 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20190321_1544'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscriber',
            new_name='Subscribers',
        ),
    ]