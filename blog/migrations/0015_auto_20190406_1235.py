# Generated by Django 2.1.7 on 2019-04-06 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20190321_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AddField(
            model_name='post',
            name='text_1',
            field=models.TextField(db_index=True, null=True, verbose_name='Текст_1'),
        ),
        migrations.AddField(
            model_name='post',
            name='text_2',
            field=models.TextField(db_index=True, null=True, verbose_name='Текст_2'),
        ),
    ]
