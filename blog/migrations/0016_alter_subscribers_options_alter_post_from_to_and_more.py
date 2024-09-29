# Generated by Django 5.1 on 2024-09-01 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20190406_1235'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscribers',
            options={'verbose_name': 'Подписчики'},
        ),
        migrations.AlterField(
            model_name='post',
            name='from_to',
            field=models.CharField(blank=True, db_index=True, max_length=200, verbose_name='Даты путешествия'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='month',
            field=models.CharField(blank=True, db_index=True, max_length=200, verbose_name='Месяц'),
        ),
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.CharField(blank=True, db_index=True, max_length=200, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text_1',
            field=models.TextField(db_index=True, default='', verbose_name='Текст_1'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='text_2',
            field=models.TextField(blank=True, db_index=True, default='', verbose_name='Текст_2'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subscribers',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]