# Generated by Django 2.0.13 on 2019-03-13 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='booking_example_1',
            field=models.TextField(blank=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='booking_example_2',
            field=models.TextField(blank=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='booking_example_3',
            field=models.TextField(blank=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='booking_example_4',
            field=models.TextField(blank=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='from_to',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='month',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='reference_1',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='reference_2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='reference_3',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='reference_4',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='reference_5',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='reference_6',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='reference_7',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='reference_8',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='text_1',
            field=models.TextField(db_index=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text_2',
            field=models.TextField(blank=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text_3',
            field=models.TextField(blank=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text_4',
            field=models.TextField(blank=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='travel_dates',
            field=models.TextField(db_index=True),
        ),
    ]
