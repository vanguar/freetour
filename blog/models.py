from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    month = models.CharField(max_length=200)
    from_to = models.CharField(max_length=200)
    text_1 = models.TextField()
    text_2 = models.TextField()
    text_3 = models.TextField()
    text_4 = models.TextField()
    booking_example_1 = models.TextField()
    booking_example_2 = models.TextField()
    booking_example_3 = models.TextField()
    booking_example_4 = models.TextField()
    travel_dates = models.TextField()
    reference_1 = models.CharField(max_length=200)
    reference_2 = models.CharField(max_length=200)
    reference_3 = models.CharField(max_length=200)
    reference_4 = models.CharField(max_length=200)
    reference_5 = models.CharField(max_length=200)
    reference_6 = models.CharField(max_length=200)
    reference_7 = models.CharField(max_length=200)
    reference_8 = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
