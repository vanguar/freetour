from django.conf import settings
from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django import forms


class Post(models.Model):
    objects = None
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name=u'Фотография', upload_to='img/%Y/%m/%d', help_text='150x150px', default="",
                                     blank=True)
    screenshot_1 = models.ImageField(verbose_name=u'Скриншот_1', upload_to='img/%Y/%m/%d', help_text='150x150px',
                                     default="", blank=True)
    screenshot_2 = models.ImageField(verbose_name=u'Скриншот_2', upload_to='img/%Y/%m/%d', help_text='150x150px',
                                     default="", blank=True)
    screenshot_3 = models.ImageField(verbose_name=u'Скриншот_3', upload_to='img/%Y/%m/%d', help_text='150x150px',
                                     default="", blank=True)
    title = models.CharField(verbose_name=u'Описание', max_length=200, db_index=True)
    slug = models.SlugField(verbose_name=u'ЧПУ', max_length=200, unique=True)
    price = models.CharField(verbose_name=u'Цена', max_length=200, db_index=True)
    month = models.CharField(verbose_name=u'Месяц', max_length=200, db_index=True)
    from_to = models.CharField(verbose_name=u'Даты путешествия', max_length=200, db_index=True)
    text_1 = models.TextField(verbose_name=u'Текст_1', db_index=True)
    text_2 = models.TextField(verbose_name=u'Текст_2', db_index=True)
    created_date = models.DateTimeField(verbose_name=u'Дата создания', default=timezone.now)
    published_date = models.DateTimeField(verbose_name=u'Дата публикации', blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})



    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']



class Subscribers(models.Model):
    name = models.CharField(max_length=120)
    username_telegram = models.CharField(max_length=120)
    departure = models.CharField(max_length=120)
    destination = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    start_date = models.CharField(max_length=120)
    final_date = models.CharField(max_length=120)
    email = models.EmailField()
    transportation_costs = models.CharField(max_length=120)
    living_expenses = models.CharField(max_length=120)


    def __str__(self):
        return "Путешественник %s %s %s %s %s %s %s %s %s %s" % (self.name, self.username_telegram,
                                                                 self.departure, self.destination, self.city,
                                                                 self.start_date, self.final_date, self.email,
                                                                 self.transportation_costs, self.living_expenses)

    class Meta:
        verbose_name = 'Подписчики'


